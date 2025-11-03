CREATE TABLE produkts (
    produktID int not null AUTO_INCREMENT,
    pris float not null,
    navn varchar(55) not null,
    status varchar(55) not null DEFAULT 'Active',
    PRimary key (produktID)
);

CREATE TABLE lagers(
    lagerID int not null AUTO_INCREMENT,
    navn varchar(55) not null,
    PRimary key (lagerID)
);

CREATE TABLE lager_manger(
    lagermangerID int not null AUTO_INCREMENT,
    lagerID int not null,
    produktID int not null,
    antal int,
    PRimary key (lagermangerID),
    
    FOREIGN KEY (lagerID) REFERENCES lagers(lagerID),
    FOREIGN KEY (produktID) REFERENCES produkts(produktID)
);
create table customers(
	customerid int not null AUTO_INCREMENT,
    navn varchar(255) not null,
    email varchar(255) not null,
    PRimary key (customerid),
    UNIQUE (email)

);
create table orders (
	OrderID int not null AUTO_INCREMENT,
    produktID int not null,
    invoicenummer int not null,
    customerid int not null,
    status varchar(55),
    mangde int not null,
    lagerID int not null,
    PRimary key (OrderID),
    
    FOREIGN KEY (produktID) REFERENCES produkts(produktID),
    FOREIGN KEY (customerid) REFERENCES customers(customerid),
    FOREIGN KEY (customerid) REFERENCES customers(customerid),
    FOREIGN key (lagerID) REFERENCES lagers(lagerID)
);

create table admin(
	adminid int not null AUTO_INCREMENT,
    navn varchar(255),
    adminpassword varchar(255),
    
    primary key (adminid)
);
