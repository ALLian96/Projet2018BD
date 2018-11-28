create table LesZones (
    noZone number (2,0),
    catZone varchar (50) not null,
    prixZone number (4,2) not null,
    constraint pk_zon_noZone primary key (noZone),
    constraint ck_zon_noZone check (noZone > 0),
    constraint ck_zon_prixZone check (prixZone >= 0),
    constraint ck_zon_cat check (catZone in ('orchestre', 'balcon', 'poulailler'))
);

create table LesTickets (
    noSpec number (4,0),
    dateRep date,
    noPlace number (3,0),
    noRang number (3,0),
    dateEmTick date,
    noDos number (3,0) not null,
    constraint pk_tck_place_rep unique (noSpec, dateRep, noPlace, noRang),
    constraint fk_tck_numS_dateR foreign key (noSpec, dateRep) references LesRepresentations_base(noSpec, dateRep),
    constraint fk_tck_noP_noR foreign key (noPlace, noRang) references LesPlaces (noPlace,noRang),
    constraint fk_tck_noD foreign key (noDos) references LesDossiers_base (noDos),
    constraint ck_dates check (dateEmTick < dateRep)
);

create table LesSpectacles (
    noSpec number (4,0),
    nomSpec varchar(50) not null,
    constraint pk_spec_noSpec primary key (noSpec),
    constraint ck_spec_noSpec check (noSpec > 0)
);

create table LesRepresentations_base (
    noSpec number (4,0),
    dateRep date,
    constraint pk_rep_noSpec_dateRep primary key (noSpec, dateRep),
    constraint fk_rep_noSpec foreign key (noSpec) references LesSpectacles(noSpec)
);

create table LesPlaces (
    noPlace number (3,0),
    noRang number (3,0),
    noZone number (2,0) not null,
    constraint pk_pl_noP_noR primary key (noPlace, noRang),
    constraint fk_pl_numZ foreign key (noZone) references LesZones(noZone),
    constraint ck_pl_noP check (noPlace > 0),
    constraint ck_pl_noR check (noRang > 0)
);

create table LesDossiers_base (
    noDos number (3,0),
    constraint pk_dos_noD primary key (noDos)
);

-- TODO 1b : ajouter la définition des vues LesDossiers et LesRepresentations

create view LesDossiers (nDos, montant) as
    with X as (select noDos, prixZone from lesZones natural join LesPlaces natural join LesTickets)
    select noDos, sum(prixZone) as montant from X group by noDos;

create view LesRepresentations (noSpec, dateRep, nbPlaces) as
    select noSpec, dateRep, nbPlaces from LesRepresentations_base where nbPlaces in (select count(noPlace) as nbPlaces from LesPlaces
             minus
               select count(noPlace) as nbPlaces from LesTickets)