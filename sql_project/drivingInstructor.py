import sqlite3 as sql

dbconnect= sql.connect('SQL/sql_project/drivingInstructors.db')
dbcursor=dbconnect.cursor()

dbcursor.execute('''
    CREATE TABLE IF NOT EXISTS B (
        ID INTEGER PRIMARY KEY,
        Name VARCHAR(255),
        Email VARCHAR(255),
        Phone_Number VARCHAR(15),
        Distance VARCHAR(20),
        Postcode VARCHAR(10)
    )
''')

# Insert data into the 'B' table
data_to_insert_B = [
('Zsolt Szlanka', 'info@primelearner.com', '07737108717', '0.6 miles (1.0 km)', 'B1 1BD'),
('Daoud Naseri', 'daoudnaseri5@gmail.com', '07429046865', '0.7 miles (1.1 km)', 'B1 1BD'),
('Saied Mohamed Shire', 'ased52@hotmail.com', '07958004574', '0.7 miles (1.1 km)', 'B1 1BD'),
('Faisal Shafiq', 'faisal@mnmdrivingschool.co.uk', '07830112698', '0.9 miles (1.4 km)', 'B1 1BD'),
('Michael Drew Reay', 'mike.reay@blueyonder.co.uk', '07778653212', '0.9 miles (1.4 km)', 'B1 1BD'),
('Natasha Harding', 'tashiba69@hotmail.com', '07956987815', '0.9 miles (1.4 km)', 'B1 1BD'),
('Deilton Parkes', 'deiltonparkes@gmail.com', '07581172113', '1.0 miles (1.6 km)', 'B1 1BD'),
('Mir Shafqat Ali', 'mirali54321@yahoo.com', '01215234175', '1.1 miles (1.8 km)', 'B1 1BD'),
('Joel Mulongeki', 'jmulongeki@outlook.com', '07902989715', '1.2 miles (1.9 km)', 'B1 1BD'),
('Abdirahman Said', 'kadawe75@hotmail.com', '07947218132', '1.3 miles (2.1 km)', 'B1 1BD'),

('Zsolt Szlanka', 'info@primelearner.com', '07737108717', '0.5 miles (0.8 km)', 'B1 1EQ'),
('Daoud Naseri', 'daoudnaseri5@gmail.com', '07429046865', '0.3 miles (0.5 km)', 'B1 1EQ'),
('Faisal Shafiq', 'faisal@mnmdrivingschool.co.uk', '07830112698', '0.6 miles (1.0 km)', 'B1 1EQ'),
('Natasha Harding', 'tashiba69@hotmail.com', '07956987815', '0.7 miles (1.1 km)', 'B1 1EQ'),
('Saied Mohamed Shire', 'ased52@hotmail.com', '07958004574', '0.7 miles (1.1 km)', 'B1 1EQ'),
('Michael Drew Reay', 'mike.reay@blueyonder.co.uk', '07778653212', '1.0 miles (1.6 km)', 'B1 1EQ'),
('Saeama Sharif', 'saimasharif3@hotmail.co.uk', '01214466939', '1.2 miles (1.9 km)', 'B1 1EQ'),
('Khalid Rafiq Khan', 'habib56789@hotmail.com', '07958618761', '1.2 miles (1.9 km)', 'B1 1EQ'),
('Deilton Parkes', 'deiltonparkes@gmail.com', '07581172113', '1.2 miles (1.9 km)', 'B1 1EQ'),
('Umar Farook', 'Info@motivatedriving.co.uk', '07365805709', '1.3 miles (2.1 km)', 'B1 1EQ'),

('Zsolt Szlanka', 'info@primelearner.com', '07737108717', '0.4 miles (0.6 km)', 'B1 1AY'),
('Saied Mohamed Shire', 'ased52@hotmail.com', '07958004574', '0.5 miles (0.8 km)', 'B1 1AY'),
('Daoud Naseri', 'daoudnaseri5@gmail.com', '07429046865', '0.5 miles (0.8 km)', 'B1 1AY'),
('Faisal Shafiq', 'faisal@mnmdrivingschool.co.uk', '07830112698', '0.6 miles (1.0 km)', 'B1 1AY'),
('Natasha Harding', 'tashiba69@hotmail.com', '07956987815', '0.7 miles (1.1 km)', 'B1 1AY'),
('Michael Drew Reay', 'mike.reay@blueyonder.co.uk', '07778653212', '0.8 miles (1.3 km)', 'B1 1AY'),
('Mir Shafqat Ali', 'mirali54321@yahoo.com', '01215234175', '1.1 miles (1.8 km)', 'B1 1AY'),
('Deilton Parkes', 'deiltonparkes@gmail.com', '07581172113', '1.2 miles (1.9 km)', 'B1 1AY'),

('Deilton Parkes', 'deiltonparkes@gmail.com', '07581172113', '0.3 miles (0.5 km)', 'B1 1BX'),
('Deepa Mahmood', 'khan_deepa@yahoo.co.uk', '07905906095', '0.4 miles (0.6 km)', 'B1 1BX'),
]

dbcursor.executemany('''
    INSERT OR IGNORE INTO B (Name, Email, Phone_Number, Distance, Postcode) VALUES (?, ?, ?, ?, ?)
''', data_to_insert_B)

dbcursor.execute('''
    CREATE TABLE IF NOT EXISTS BA (
        ID INTEGER PRIMARY KEY,
        Name VARCHAR(255),
        Email VARCHAR(255),
        Phone_Number VARCHAR(15),
        Distance VARCHAR(20),
        Postcode VARCHAR(10)
    )
''')

data_to_insert_BA = [
 ('Gary Norcott', 'garynorcott@rocketmail.com', '07870380262', '0.2 miles (0.3 km)', 'BA1 0AY'),
('Stephen Kyriacos Paraskeva', 'stephenparaskeva@aol.com', '07738461164', '1.3 miles (2.1 km)', 'BA1 0AY'),
('Basil Thompson', 'info@basilll.co.uk', '01225482095', '1.3 miles (2.1 km)', 'BA1 0AY'),
('Martin Dover', 'tallbloke64@msn.com', '07795423037', '1.4 miles (2.2 km)', 'BA1 0AY'),
('Giselle Pascale Le Fort', 'giselle@lefort.co.uk', '07801277497', '1.5 miles (2.4 km)', 'BA1 0AY'),
('Luke J. Corbett', 'lukejcorbett@yahoo.co.uk', '07810880262', '1.5 miles (2.4 km)', 'BA1 0AY'),
('Patrick Hinton', 'paddy@paddyhinton.co.uk', '07951187822', '1.6 miles (2.6 km)', 'BA1 0AY'),
('Graham Raymond Willis', 'grahamwillis1958@googlemail.com', '01225840699', '2.0 miles (3.2 km)', 'BA1 0AY'),
('Mark David Melbourne', 'mdmelbourne@hotmail.co.uk', '07767300700', '2.1 miles (3.4 km)', 'BA1 0AY'),
('Jashim Ahmed', '', '07914422250', '2.3 miles (3.7 km)', 'BA1 0AY'),
('Gary Norcott', 'garynorcott@rocketmail.com', '07870380262', '0.2 miles (0.3 km)', 'BA1 0AZ'),
('Stephen Kyriacos Paraskeva', 'stephenparaskeva@aol.com', '07738461164', '1.3 miles (2.1 km)', 'BA1 0AZ'),
('Basil Thompson', 'info@basilll.co.uk', '01225482095', '1.3 miles (2.1 km)', 'BA1 0AZ'),
('Martin Dover', 'tallbloke64@msn.com', '07795423037', '1.4 miles (2.2 km)', 'BA1 0AZ'),
('Giselle Pascale Le Fort', 'giselle@lefort.co.uk', '07801277497', '1.5 miles (2.4 km)', 'BA1 0AZ'),
('Luke J. Corbett', 'lukejcorbett@yahoo.co.uk', '07810880262', '1.5 miles (2.4 km)', 'BA1 0AZ'),
('Patrick Hinton', 'paddy@paddyhinton.co.uk', '07951187822', '1.6 miles (2.6 km)', 'BA1 0AZ'),
('Graham Raymond Willis', 'grahamwillis1958@googlemail.com', '01225840699', '2.0 miles (3.2 km)', 'BA1 0AZ'),
('Mark David Melbourne', 'mdmelbourne@hotmail.co.uk', '07767300700', '2.1 miles (3.4 km)', 'BA1 0AZ'),
('Jashim Ahmed', '', '07914422250', '2.3 miles (3.7 km)', 'BA1 0AZ'),
('Gary Norcott', 'garynorcott@rocketmail.com', '07870380262', '0.2 miles (0.3 km)', 'BA1 0BT'),
('Stephen Kyriacos Paraskeva', 'stephenparaskeva@aol.com', '07738461164', '1.3 miles (2.1 km)', 'BA1 0BT'),
('Basil Thompson', 'info@basilll.co.uk', '01225482095', '1.3 miles (2.1 km)', 'BA1 0BT'),
('Martin Dover', 'tallbloke64@msn.com', '07795423037', '1.4 miles (2.2 km)', 'BA1 0BT'),
('Giselle Pascale Le Fort', 'giselle@lefort.co.uk', '07801277497', '1.5 miles (2.4 km)', 'BA1 0BT'),
('Luke J. Corbett', 'lukejcorbett@yahoo.co.uk', '07810880262', '1.5 miles (2.4 km)', 'BA1 0BT'),
('Patrick Hinton', 'paddy@paddyhinton.co.uk', '07951187822', '1.6 miles (2.6 km)', 'BA1 0BT'),
('Graham Raymond Willis', 'grahamwillis1958@googlemail.com', '01225840699', '2.0 miles (3.2 km)', 'BA1 0BT'),
('Mark David Melbourne', 'mdmelbourne@hotmail.co.uk', '07767300700', '2.1 miles (3.4 km)', 'BA1 0BT'),
('Jashim Ahmed', '', '07914422250', '2.3 miles (3.7 km)', 'BA1 0BT'),
('Gary Norcott', 'garynorcott@rocketmail.com', '07870380262', '0.2 miles (0.3 km)', 'BA1 0EJ'),
('Stephen Kyriacos Paraskeva', 'stephenparaskeva@aol.com', '07738461164', '1.3 miles (2.1 km)', 'BA1 0EJ'),
('Basil Thompson', 'info@basilll.co.uk', '01225482095', '1.3 miles (2.1 km)', 'BA1 0EJ'),
('Martin Dover', 'tallbloke64@msn.com', '07795423037', '1.4 miles (2.2 km)', 'BA1 0EJ'),
('Giselle Pascale Le Fort', 'giselle@lefort.co.uk', '07801277497', '1.5 miles (2.4 km)', 'BA1 0EJ'),
('Luke J. Corbett', 'lukejcorbett@yahoo.co.uk', '07810880262', '1.5 miles (2.4 km)', 'BA1 0EJ'),
('Patrick Hinton', 'paddy@paddyhinton.co.uk', '07951187822', '1.6 miles (2.6 km)', 'BA1 0EJ'),

]

dbcursor.executemany('''
    INSERT OR IGNORE INTO BA (Name, Email, Phone_Number, Distance, Postcode) VALUES (?, ?, ?, ?, ?)
''', data_to_insert_BA)



dbconnect.commit()
dbconnect.close()