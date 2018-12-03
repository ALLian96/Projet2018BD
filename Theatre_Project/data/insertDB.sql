insert into LesSpectacles(noSpec, nomSpec) values (1, 'How to be a Parisian?');
insert into LesSpectacles(noSpec, nomSpec) values (2, 'Je parle toute seule');
insert into LesSpectacles(noSpec, nomSpec) values (3, 'Une semaine pas plus');

insert into LesZones(noZone, catZone, prixZone) values (1, 'orchestre', 5);
insert into LesZones(noZone, catZone, prixZone) values (2, 'balcon', 3.5);
insert into LesZones(noZone, catZone, prixZone) values (3, 'poulailler', 10);


insert into LesPlaces(noPlace, noRang, noZone) values (1, 1, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (2, 1, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (3, 1, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (4, 1, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (5, 1, 1);

insert into LesPlaces(noPlace, noRang, noZone) values (1, 2, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (2, 2, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (3, 2, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (4, 2, 1);
insert into LesPlaces(noPlace, noRang, noZone) values (5, 2, 1);

insert into LesPlaces(noPlace, noRang, noZone) values (1, 3, 2);
insert into LesPlaces(noPlace, noRang, noZone) values (2, 3, 2);
insert into LesPlaces(noPlace, noRang, noZone) values (3, 3, 2);
insert into LesPlaces(noPlace, noRang, noZone) values (4, 3, 2);
insert into LesPlaces(noPlace, noRang, noZone) values (5, 3, 2);
insert into LesPlaces(noPlace, noRang, noZone) values (6, 3, 3);
insert into LesPlaces(noPlace, noRang, noZone) values (7, 3, 3);

insert into LesUsers(login, nom, prenom, mail, mdp) values ( 'Abb','Berjon','Anne','ab@gmail.com','123456');
insert into LesUsers(login, nom, prenom, mail, mdp) values ('Brr','Royer','Benoit','br@hotmail.fr','654321');

insert into LesDossiers_base(noDos,login) values (1,'Abb');
insert into LesDossiers_base(noDos,login) values (2,'Abb');
insert into LesDossiers_base(noDos,login) values (3,'Abb');
insert into LesDossiers_base(noDos,login) values (4,'Abb');
insert into LesDossiers_base(noDos,login) values (5,'Brr');
insert into LesDossiers_base(noDos,login) values (6,'Brr');
insert into LesDossiers_base(noDos,login) values (7,'Brr');

insert into LesRepresentations_base(noSpec, dateRep) values (1, '24/01/2018 17:00');
insert into LesRepresentations_base(noSpec, dateRep) values (1, '25/01/2018 20:00');
insert into LesRepresentations_base(noSpec, dateRep) values (1, '26/01/2018 21:00');
insert into LesRepresentations_base(noSpec, dateRep) values (2, '24/01/2018 21:00');
insert into LesRepresentations_base(noSpec, dateRep) values (2, '25/01/2018 23:00');
insert into LesRepresentations_base(noSpec, dateRep) values (3, '20/02/2018 18:00');
insert into LesRepresentations_base(noSpec, dateRep) values (3, '21/02/2018 18:30');
insert into LesRepresentations_base(noSpec, dateRep) values (3, '22/02/2018 22:00');

-- Tickets
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (1, '24/01/2018 17:00', 1, 1, '23/01/2018 21:30:20',1);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (1, '24/01/2018 17:00', 2, 1, '23/01/2018 21:30:20',1);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (1, '24/01/2018 17:00', 3, 1, '23/01/2018 21:30:20',1);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (1, '24/01/2018 17:00', 4, 1, '23/01/2018 21:30:20',1);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (1, '24/01/2018 17:00', 5, 1, '23/01/2018 21:30:20',1);

insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (2, '25/01/2018 23:00', 1, 2, '20/01/2018 22:31:00',2);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (2, '25/01/2018 23:00', 2, 2, '20/01/2018 22:31:00',2);

insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (2, '25/01/2018 23:00', 1, 3, '20/01/2018 14:22:00',3);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (2, '25/01/2018 23:00', 2, 3, '20/01/2018 14:22:00',3);

insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (2, '25/01/2018 23:00', 6, 3, '24/01/2018 22:00:00',4);

insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (3, '20/02/2018 18:00', 7, 3, '10/02/2018 22:10:00',5);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (3, '20/02/2018 18:00', 6, 3, '10/02/2018 22:15:00',5);

insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (3, '22/02/2018 22:00', 2, 2, '14/02/2018 22:00:00',6);
insert into LesTickets(noSpec, dateRep, noPlace, noRang, dateEmTick, noDos) values (3, '22/02/2018 22:00', 3, 2, '14/02/2018 22:05:00',6);

-- Reservations

insert into LesReservations(noSpec, dateRep, noPlace, noRang, dateReserve, login) values (1, '24/01/2018 17:00', 1, 1, '22/01/2018 15:15:00','Abb');
insert into LesReservations(noSpec, dateRep, noPlace, noRang, dateReserve, login) values (1, '24/01/2018 17:00', 2, 1, '22/01/2018 15:15:00','Abb');

insert into LesReservations(noSpec, dateRep, noPlace, noRang, dateReserve, login) values (2, '25/01/2018 23:00', 1, 2, '20/01/2018 22:31:00','Abb');

insert into LesReservations(noSpec, dateRep, noPlace, noRang, dateReserve, login) values (3, '20/02/2018 18:00', 7, 3,'06/02/2018 15:15:00','Brr');
insert into LesReservations(noSpec, dateRep, noPlace, noRang, dateReserve, login) values (3, '20/02/2018 18:00', 6, 3,'06/02/2018 15:30:00','Brr');

insert into LesReservations(noSpec, dateRep, noPlace, noRang, dateReserve, login) values (3, '22/02/2018 22:00', 2, 2,'22/01/2018 17:00:00','Brr');
insert into LesReservations(noSpec, dateRep, noPlace, noRang, dateReserve, login) values (3, '22/02/2018 22:00', 3, 2,'22/01/2018 17:00:00','Brr');