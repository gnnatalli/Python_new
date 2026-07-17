HOST = ''
USER = ''
PASSWORD = ''
DATABASE = 'sakila'

HOST_WRITE = ''
USER_WRITE = ''
PASSWORD_WRITE = ''

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

