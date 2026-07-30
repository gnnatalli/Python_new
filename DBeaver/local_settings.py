HOST = 'ich-db.edu.itcareerhub.de'
USER = 'ich1'
PASSWORD = 'password_ich1'
DATABASE = 'sakila'

HOST_WRITE = 'ich-edit.edu.itcareerhub.de'
USER_WRITE = 'ich1'
PASSWORD_WRITE = 'ich_edit_password_ilovedbs'

# ВНИМАНИЕ!!! Заменить на СВОЮ БД!!!
DATABASE_WRITE = '060326_ptm_Naty'

dbconfig = {
'host': HOST,
'user': USER,
'password': PASSWORD,
'database': DATABASE,
}

dbconfig_write = {
'host': HOST_WRITE,
'user': USER_WRITE,
'password': PASSWORD_WRITE,
'database': DATABASE_WRITE,
}



MONGODB_URL_READ = 'mongodb://ich1:password@mongo.itcareerhub.de/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich'
MONGODB_URL_WRITE = 'mongodb://ich_editor:verystrongpassword@mongo.edu.itcareerhub.de:27017/?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit'

MONGODB_URL_ATLAS = 'mongodb+srv://gnnatalli_db_user:GNHjync8HB3yAv4H@naty.wzzlhmo.mongodb.net/'

