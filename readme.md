# Precisa adicionar os repositorios

# Precisa dos dados

# Precisa rodar o mongodb
https://v16-webapp.tiktok.com/bd24dc9ece13ccb6bc73e02255d90ed7/638930a6/video/tos/useast2a/tos-useast2a-ve-0068c004/b1e08712e67e436c862e1eee97e105ee/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=3172&bt=1586&cs=0&ds=3&ft=4b~OyMXh8Zmo0xTTx64jV5dgZpWrKsdm&mime_type=video_mp4&qs=0&rc=Ozo4NGY8ZTc5MzZoZDU4NUBpM3Bnc2g6Znd5ZjMzNzczM0AvYDFgXjAyXjUxXmMyMmEtYSMvaTBycjRvaXJgLS1kMTZzcw%3D%3D&l=202212011652210102170541701ED76CEA&btag=80000


# download the need repositories

# creating volume
docker volume create my_test_volume --opt type=none --opt device=dados_gian_mongo_arrumados/ --opt o=bind 

# connecting
<!-- 
docker run -v ~/docker --name mongodb -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=balta -e MONGO_INITDB_ROOT_PASSWORD=e296cd9f mongo

docker run -p 8888:8888 -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=balta -e MONGO_INITDB_ROOT_PASSWORD=e296cd9f -v my_test_volume:/data/db "teste"
 -->

docker run -p 8888:8888 -p 27017:27017 -v C:\doutorado\software\EthoWatcherOS-docker\dados_gian_mongo_arrumados\:/data/db "teste"


