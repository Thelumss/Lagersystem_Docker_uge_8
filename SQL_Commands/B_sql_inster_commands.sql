insert into produkts(pris, navn, status)
value(3.69,"Duck - Breast", "Active");

insert into produkts(pris, navn, status)
value(9.75,"Seabream Whole Farmed", "Active");

insert into produkts(pris, navn, status)
value(0.35,"Wine - Red, Lurton Merlot De", "Active");

insert into produkts(pris, navn, status)
value(2.39,"Artichoke - Hearts, Canned", "Active");

insert into produkts(pris, navn, status)
value(5.44,"Rum - Spiced, Captain Morgan", "Active");

insert into produkts(pris, navn, status)
value(5.43,"Cheese Cloth No 100", "Inactive");

insert into lagers(navn)
value("odense");

insert into lagers(navn)
value("københavn");

insert into lagers(navn)
value("århus");

insert into lager_manger(lagerID,produktID,antal)
value(1,1,20);
insert into lager_manger(lagerID,produktID,antal)
value(1,2,10);
insert into lager_manger(lagerID,produktID,antal)
value(1,3,6);
insert into lager_manger(lagerID,produktID,antal)
value(1,4,100);

insert into lager_manger(lagerID,produktID,antal)
value(2,1,22);
insert into lager_manger(lagerID,produktID,antal)
value(2,2,103);
insert into lager_manger(lagerID,produktID,antal)
value(2,3,62);
insert into lager_manger(lagerID,produktID,antal)
value(2,4,1);

insert into lager_manger(lagerID,produktID,antal)
value(3,1,203);
insert into lager_manger(lagerID,produktID,antal)
value(3,2,102);
insert into lager_manger(lagerID,produktID,antal)
value(3,3,66);
insert into lager_manger(lagerID,produktID,antal)
value(3,4,10);


insert into customers(navn,email)
value("luke","luke@test.com");
insert into customers(navn,email)
value("test","test@test.com");
insert into customers(navn,email)
value("dennis","dennis@test.com");
insert into customers(navn,email)
value("Viktor","Viktor@test.com");

insert into orders(produktID,invoicenummer,customerid,status,mangde,lagerID)
value(5,1000,1,"good",10,1);
insert into orders(produktID,invoicenummer,customerid,status,mangde,lagerID)
value(1,1004,4,"good",4,2);
insert into orders(produktID,invoicenummer,customerid,status,mangde,lagerID)
value(3,1004,4,"good",3,2);
insert into orders(produktID,invoicenummer,customerid,status,mangde,lagerID)
value(5,1003,3,"good",30,3);
insert into orders(produktID,invoicenummer,customerid,status,mangde,lagerID)
value(2,1003,3,"bad",12,3);
insert into orders(produktID,invoicenummer,customerid,status,mangde,lagerID)
value(2,1004,4,"good",1,3);
insert into orders(produktID,invoicenummer,customerid,status,mangde,lagerID)
value(5,1005,4,"good",4,1);
insert into orders(produktID,invoicenummer,customerid,status,mangde,lagerID)
value(5,1002,2,"good",12,1);
insert into orders(produktID,invoicenummer,customerid,status,mangde,lagerID)
value(3,1002,2,"good",14,1);
insert into orders(produktID,invoicenummer,customerid,status,mangde,lagerID)
value(2,1002,2,"good",11,1);