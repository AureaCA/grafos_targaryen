

CREATE (a:Personaje {nombre: 'Aegon I Targaryen',nacimiento:'27 ac',
                    muerte:'37 dc',ojos:'morados',cabello:'plateado-dorado',
                    espada:'Blackfyre',titulos:'Rey de los Siete Reinos, Señor de Rocadragón',
                    genero:'masculino',apodo:'Aegon el Conquistador'}),
      
       (b:Personaje {nombre: 'Visenya Targaryen',nacimiento:'29 ac',
                    muerte:'44 dc',ojos:'morados',cabello:'plateado-dorado',
                    espada:'Dark Sister',titulos:'Señora de Rocadragón,Reina, Reina Dowager',
                    genero:'femenino'}),
       (c:Personaje {nombre: 'Rhaenys I Targaryen',nacimiento:'25 ac',
                    muerte:'10 dc',ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Reina, Señora de Rocadragón',genero:'femenino'}),
       (d:Personaje {nombre: 'Aerion Targaryen',nacimiento:'75-49 ac en Rocadragón',muerte:'27-2 dc en Rocadragón',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Señor de Rocadragón',genero:'masculino'}),
       (e:Personaje {nombre: 'Valaena Velaryon',nacimiento:'78-40 ac en Marcaderiva',muerte:'26 dc en Rocadragón',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Señora de Rocadragón',genero:'femenino'}),
       (f:Personaje {nombre: 'Orys Baratheon',nacimiento:'20 ac',muerte:'37 dc en Bastión de Tormentas',
                    ojos:'negros',cabello:'negro',
                    titulos:'Señor de Bastión de Tormentas, Mano del rey',genero:'masculino',apodo:'Orys una mano'}),
       (g:Personaje {nombre: 'Daemion Targaryen',nacimiento:'87-53 ac en Rocadragón',muerte:'desconocido',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Señor de Rocadragón',genero:'masculino'}),
       (h:Personaje {nombre: 'Aerys Targaryen',nacimiento:'101-67 ac en Rocadragón',muerte:'desconocido',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Señor de Rocadragón',genero:'masculino'}),
       (i:Personaje {nombre: 'Aegon Targaryen (Siglo de sangre)',nacimiento:'114-80 ac en Rocadragón',muerte:'desconocido',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Señor de Rocadragón',genero:'masculino'}),
       (j:Personaje {nombre: 'Elaena I Targaryen',nacimiento:'114-80 ac en Rocadragón',muerte:'desconocido',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Señora de Rocadragón',genero:'femenino'}),
       (k:Personaje {nombre: 'Gaemon Targaryen (Siglo de sangre)',nacimiento:'desconocido en Rocadragón',muerte:'101 ac en Rocadragón',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Señor de Rocadragón',genero:'masculino',apodo:'Gaemon el Glorioso'}),
       (l:Personaje {nombre: 'Daenys Targaryen',nacimiento:'126 ac en Valyria',muerte:'101 ac  en Rocadragón',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Señora de Rocadragón',genero:'femenino',apodo:'Daenys la Soñadora'}),
       (m:Personaje {nombre: 'Aenar Targaryen',nacimiento:'138 ac en Valyria',muerte:'102 ac  en Rocadragón',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Señor de Rocadragón, Dragonlord',genero:'masculino',apodo:'Aenar el Exiliado'}),
       (n:Grupo{nombre:'Siglo Sangriento'}),
       
       
       (a)-[:Hermanos]->(b),
       (a)-[:Hermanos]->(c),
       (b)-[:Hermanos]->(c),
       (d)-[:Padre]->(a),
       (d)-[:Padre]->(b),
       (d)-[:Padre]->(c),
       (d)-[:Padre]->(f),
       (e)-[:Padre]->(a),
       (e)-[:Padre]->(b),
       (e)-[:Padre]->(c),
       (g)-[:Padre]->(d),
       (h)-[:Padre]->(g),
       (i)-[:Padre]->(h),
       (j)-[:Padre]->(h),
       (k)-[:Padre]->(j),
       (k)-[:Padre]->(i),
       (j)-[:Hermanos]->(i),
       (j)-[:Esposos]->(i),
       (l)-[:Esposos]->(k),
       (l)-[:Hermanos]->(k),
       (l)-[:Padre]->(j),
       (l)-[:Padre]->(i),
       (m)-[:Padre]->(k),
       (m)-[:Padre]->(l),
       (a)-[:Integrante]->(n),
       (b)-[:Integrante]->(n),
       (c)-[:Integrante]->(n),
       (d)-[:Integrante]->(n),
       (e)-[:Integrante]->(n),
       (f)-[:Integrante]->(n),
       (g)-[:Integrante]->(n),
       (h)-[:Integrante]->(n),
       (i)-[:Integrante]->(n),
       (j)-[:Integrante]->(n),
       (k)-[:Integrante]->(n),
       (l)-[:Integrante]->(n),
       (m)-[:Integrante]->(n);
       


MERGE (start:Personaje {nombre: 'Aegon Targaryen (Siglo de sangre)'})
MERGE (end:Personaje {nombre: 'Elaena I Targaryen'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Aegon Targaryen (Siglo de sangre)'})
MERGE (end:Personaje {nombre: 'Elaena I Targaryen'})
MERGE (start)-[:Hermanos]-(end); 

MERGE (start:Personaje {nombre: 'Aerion Targaryen'})
MERGE (end:Personaje {nombre: 'Valaena Velaryon'})
MERGE (start)-[:Esposos]-(end);       
       
   

MERGE (start:Personaje {nombre: 'Aegon I Targaryen'})
MERGE (end:Personaje {nombre: 'Visenya Targaryen'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Aegon I Targaryen'})
MERGE (end:Personaje {nombre: 'Rhaenys I Targaryen'})
MERGE (start)-[:Esposos]-(end);


MERGE (n:Personaje {nombre: 'Maegor Targaryen',nacimiento:'12 dc',muerte:'48 dc',
                    ojos:'morados',cabello:'plateado-dorado',espada:'Dark Sister, Blackfyre',
                    titulos:'Principe, Mano del Rey, Rey',genero:'masculino',
                    apodo:'Maegor el Cruel'});
MERGE (n:Personaje {nombre: 'Aenys I Targaryen',nacimiento:'7 dc',muerte:'42 dc',
                    ojos:'morados',cabello:'plateado-dorado',espada:'Blackfyre',apodo:'Aenys el débil',
                    titulos:'Principe, Rey',genero:'masculino'});

MERGE (start:Personaje {nombre: 'Maegor Targaryen'})
MERGE (end:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (start)-[:Hermanos]-(end);

MERGE (n:Personaje {nombre: 'Alyssa Velaryon',nacimiento:'7 dc',muerte:'54 dc',
                    ojos:'morados',cabello:'plateado',
                    titulos:'Reina, Reina Dowager, Reina Regente, Señora de Bastión de Tormentas',
                    genero:'femenino'});
CREATE (a:Personaje {nombre: 'Rhaena I Targaryen',nacimiento:'23 dc',muerte:'73 dc',
                    ojos:'lila',cabello:'plateado-dorado',
                    titulos:'Princesa',
                    genero:'femenino',apodo:'La Reina en el Este, Señora de Harrenhal'}),
       (b:Personaje {nombre: 'Aegon Targaryen (el No Coronado)',nacimiento:'26 dc',muerte:'43 dc',
                    ojos:'lila',cabello:'plateado',titulos:'Principe de Rocadragón',
                    genero:'masculino',apodo:'Aegon el No Coronado'}),
       (c:Personaje {nombre: 'Viserys Targaryen',nacimiento:'29 AC',muerte:'44 AC',
                     ojos:'morados',cabello:'plateado',titulos:'Principe',genero:'masculino'}),
       (d:Personaje {nombre: 'Jaeharys I Targaryen',apodo:'Jaeharys el Conciliador,El Rey Viejo',
                     genero:'masculino',nacimiento:'34 AC',muerte:'103 AC',ojos:'morados',
                     titulos:'Principe, Rey de los Siete Reinos'}),
       (e:Personaje {nombre: 'Alysanne Targaryen',apodo:'Buena Reina Alysanne',
                     genero:'femenino',nacimiento:'36 AC',muerte:'100 AC',titulos:'Princesa,Reina',
                     ojos:'azules',cabello:'rubio'}),
       (n:Grupo {nombre: 'Los Hijos y Nietos del Dragón'}),
       
       (a)-[:Hermanos]->(b),
       (a)-[:Hermanos]->(c),
       (a)-[:Hermanos]->(d),
       (a)-[:Hermanos]->(e),
       (b)-[:Hermanos]->(c),
       (b)-[:Hermanos]->(d),
       (b)-[:Hermanos]->(e),
       (c)-[:Hermanos]->(d),
       (c)-[:Hermanos]->(e),
       (d)-[:Hermanos]->(e),
       (a)-[:Integrante]->(n),
       (b)-[:Integrante]->(n),
       (c)-[:Integrante]->(n),
       (d)-[:Integrante]->(n),
       (e)-[:Integrante]->(n);
       


MERGE (c:Personaje {nombre: 'Aerea Targaryen',nacimiento:'42 AC',muerte:'56 AC',
                    ojos:'lila',cabello:'plateado-dorado',titulos:'Princesa',genero:'femenino'});
MERGE (n:Personaje {nombre: 'Rhaella Targaryen',nacimiento:'42 AC',muerte:'73 AC',
                    ojos:'lila',cabello:'plateado',titulos:'Princesa',genero:'femenino'});

MERGE (start:Personaje {nombre: 'Aerea Targaryen'})
MERGE (end:Personaje {nombre: 'Rhaella Targaryen'})
MERGE (start)-[:Hermanos]-(end);

MERGE (n:Grupo {nombre: 'The Black Brides'});
MERGE (n:Personaje {nombre: 'Ceryse Hightower',nacimiento:'2 AC',muerte:'45 AC',
                    ojos:'azules',cabello:'rubio',
                    titulos:'Reina', genero:'femenino'});
MERGE (n:Personaje {nombre: 'Alys Harroway',nacimiento:'desconocido',muerte:'44 AC',
                    ojos:'cafés',cabello:'castaño',
                    titulos:'Reina', genero:'femenino'});
MERGE (n:Personaje {nombre: 'Tyanna of the Tower',nacimiento:'desconocido',muerte:'48 AC',
                    ojos:'claros',cabello:'negro',
                    titulos:'Reina, Señora de los susurros,Tyanna de Pentos',
                    genero:'femenino'});
MERGE (n:Personaje {nombre: 'Elinor Costayne',nacimiento:'28 AC',muerte:'desconocido',
                    ojos:'claros',cabello:'pelirrojo',
                    titulos:'Reina',genero:'femenino'});
MERGE (n:Personaje {nombre: 'Jeyne Westerling',nacimiento:'27 AC',muerte:'47',
                    ojos:'desconocido',cabello:'castaño',
                    titulos:'Reina, Señora de Tarbeck Hall',genero:'femenino'});

MERGE (n:Grupo {nombre: 'Era del Rey Viejo'});
CREATE (a:Personaje {nombre: 'Daenerys Targaryen',nacimiento:'53 AC',muerte:'60',
                    ojos:'morados',cabello:'plateado',
                    titulos:'Princesa',genero:'femenino'}),
       (b:Personaje {nombre: 'Aemon Targaryen',nacimiento:'55 AC',muerte:'92',
                    ojos:'lila',cabello:'plateado',
                    titulos:'Principe, Principe de Rocadragón, Maestro de leyes,Señor Justiciador',
                    genero:'masculino'}),
       (c:Personaje {nombre: 'Baelon Targaryen',nacimiento:'57 AC',muerte:'101 AC',
                    ojos:'morados',cabello:'plateado',
                    titulos:'Principe de Rocadragón, Mano del Rey',apodo:'Baelon el valiente',
                    genero:'masculino',espada:'Dark Sister'}),
       (d:Personaje {nombre: 'Alyssa Targaryen',nacimiento:'60 AC',muerte:'84 AC',
                    ojos:'heterocromia violeta y verde',cabello:'rubio oscuro',
                    titulos:'Princesa',genero:'femenino'}),
       (e:Personaje {nombre: 'Maegelle Targaryen',nacimiento:'62 AC',muerte:'96 AC',
                    ojos:'morado',cabello:'plateado',
                    titulos:'Princesa,Septa', genero:'femenino'}),
       (f:Personaje {nombre: 'Vaegon Targaryen',nacimiento:'63 AC',muerte:'101 AC o después',
                    ojos:'lila',cabello:'plateado-dorado',
                    titulos:'Principe, Archimaestre de matematicas',
                    genero:'masculino',apodo:'Vaegon el Sin Dragón'}),
       (g:Personaje {nombre: 'Daella Targaryen',nacimiento:'64 AC',muerte:'82 AC en el Valle de Arryn (posparto)',
                    ojos:'morados',cabello:'plateado',
                    titulos:'Princesa, Señora de Eyrie', genero:'femenino'}),
       (h:Personaje {nombre: 'Saera Targaryen',nacimiento:'67 AC',muerte:'101 AC o después',
                    ojos:'morados',cabello:'plateado',
                    titulos:'Princesa', genero:'femenino'}),
       (i:Personaje {nombre: 'Viserra Targaryen',nacimiento:'71 AC',muerte:'87 AC',
                    ojos:'lila',cabello:'plateado-dorado',
                    titulos:'Princesa',
                    genero:'femenino'}),
       (j:Personaje {nombre: 'Gael Targaryen',nacimiento:'80 AC',muerte:'99 AC',
                    ojos:'morados',cabello:'plateado',
                    titulos:'Princesa',
                    genero:'masculino',apodo:'La niña del invierno'}),
       (a)-[:Hermanos]->(b),
       (a)-[:Hermanos]->(c),
       (a)-[:Hermanos]->(d),
       (a)-[:Hermanos]->(e),
       (a)-[:Hermanos]->(f),
       (a)-[:Hermanos]->(g),
       (a)-[:Hermanos]->(h),
       (a)-[:Hermanos]->(i),
       (a)-[:Hermanos]->(j),
       (b)-[:Hermanos]->(c),
       (b)-[:Hermanos]->(d),
       (b)-[:Hermanos]->(e),
       (b)-[:Hermanos]->(f),
       (b)-[:Hermanos]->(g),
       (b)-[:Hermanos]->(h),
       (b)-[:Hermanos]->(i),
       (b)-[:Hermanos]->(j),
       (c)-[:Hermanos]->(d),
       (c)-[:Hermanos]->(e),
       (c)-[:Hermanos]->(f),
       (c)-[:Hermanos]->(g),
       (c)-[:Hermanos]->(h),
       (c)-[:Hermanos]->(i),
       (c)-[:Hermanos]->(j),
       (d)-[:Hermanos]->(e),
       (d)-[:Hermanos]->(f),
       (d)-[:Hermanos]->(g),
       (d)-[:Hermanos]->(h),
       (d)-[:Hermanos]->(i),
       (d)-[:Hermanos]->(j),
       (e)-[:Hermanos]->(f),
       (e)-[:Hermanos]->(g),
       (e)-[:Hermanos]->(h),
       (e)-[:Hermanos]->(i),
       (e)-[:Hermanos]->(j),
       (f)-[:Hermanos]->(g),
       (f)-[:Hermanos]->(h),
       (f)-[:Hermanos]->(i),
       (f)-[:Hermanos]->(j),
       (g)-[:Hermanos]->(h),
       (g)-[:Hermanos]->(i),
       (g)-[:Hermanos]->(j),
       (h)-[:Hermanos]->(j);


MERGE (n:Personaje {nombre: 'Jocelyn Baratheon',nacimiento:'54 AC',muerte:'92-129 AC',
                    ojos:'oscuros',cabello:'negro',
                    titulos:'Señora',genero:'femenino'});
MERGE (n:Personaje {nombre: 'Boremund Baratheon',nacimiento:'52 AC',muerte:'101-129',
                    ojos:'oscuros',cabello:'negro',
                    titulos:'Señor de Bastión de Tormentas, Señor de Paramount of the Stormlands',
                    genero:'masculino'});

MERGE (start:Personaje {nombre: 'Jocelyn Baratheon'})
MERGE (end:Personaje {nombre: 'Boremund Baratheon'})
MERGE (start)-[:Hermanos]-(end);



MERGE (n:Dragon {nombre: 'Balerion',apodo:'el terror negro',nacimiento:'114 a.c en Valyria',muerte:'94 d.c',color:'negro',genero:'macho'});
MERGE (n:Dragon {nombre: 'Vhagar',nacimiento:'114-88 a.c en Dragonstone',muerte:'130 d.c en las Tierras de los Ríos (Ojo de Dioses)',color:'cobre con brillo verdoso azul',ojos:'dorados',genero:'hembra'});
MERGE (n:Dragon {nombre: 'Meraxes',nacimiento:'52 a.c en Dragonstone',muerte:'10 d.c en Dorne (Sotoinfierno)',color:'plateado',ojos: 'dorados',genero:'hembra'});
MERGE (n:Dragon {nombre: 'Quicksilver',nacimiento:'7 d.c en Dragonstone',muerte:'43 d.c en las Tierras de los Ríos (Ojo de Dioses)',color:'plateado',ojos: 'desconocido',genero:'hembra'});
MERGE (n:Dragon {nombre: 'Meleys',apodo:'la Reina Roja',nacimiento:'75 d.c en Dragonstone',muerte:'129 d.c en las Tierras de la Corona (Reposo del Grajo)',color:'rojo y rosa',ojos: 'desconocido',genero:'hembra'});
MERGE (n:Dragon {nombre: 'Vermithor',apodo:'la Furia de Bronze',nacimiento:'34 d.c en Dragonstone',muerte:'130 d.c en el Dominio (Ladera)',color:'bronze',ojos: 'desconocido',genero:'macho'});
MERGE (n:Dragon {nombre: 'Silverwing',nacimiento:'36-42 d.c en Desembarco del Rey',muerte:'136-153 d.c ',color:'plateado',ojos: 'desconocido',genero:'hembra'});
MERGE (n:Dragon {nombre: 'Dreamfyre',nacimiento:'32 d.c',muerte:'130 d.c en Desembarco del Rey',color:'azul claro con plateado',ojos: 'desconocido',genero:'hembra'});
MERGE (n:Dragon {nombre: 'Caraxes',apodo:'el Anfiptero de Sangre',nacimiento:'72 dc',muerte:'130 d.c en el Ojo de Dioses',color:'rojo',ojos: 'desconocido',genero:'macho'});
MERGE (n:Dragon {nombre: 'Moondancer',nacimiento:'desconocido',muerte:'130 d.c en Rocadragón',color:'verde claro',ojos: 'desconocido',genero:'hembra'});
MERGE (n:Dragon {nombre: 'Syrax',nacimiento:'desconocido',muerte:'130 d.c en Desembarco del Rey',color:'amarillo',ojos: 'desconocido',genero:'hembra'});
MERGE (n:Dragon {nombre: 'Seasmoke',nacimiento:'101 d.c en Dragonstone',muerte:'130 d.c en el Dominio (Ladera)',color:'plateado gris',ojos: 'desconocido',genero:'macho'});
MERGE (n:Dragon {nombre: 'Vermax',nacimiento:'114-120 d.c',muerte:'130 d.c en el Gaznate',color:'verde olivo',ojos: 'desconocido',genero:'macho'});
MERGE (n:Dragon {nombre: 'Arrax',nacimiento:'115-120 dc',muerte:'129 d.c en la Bahía de los Naufragios',color:'blanco perla',ojos: 'dorados',genero:'macho'});
MERGE (n:Dragon {nombre: 'Tyraxes',nacimiento:'117-120 d.c ',muerte:'130 d.c en Desembarco del Rey',color:'desconocido',ojos: 'desconocido',genero:'macho'});
MERGE (n:Dragon {nombre: 'Sunfyre',apodo:'el dorado',nacimiento:'desconocido en Rocadragón ',muerte:'130 d.c en Desembarco del Rey',color:'dorado',ojos: 'desconocido',genero:'macho'});
MERGE (n:Dragon {nombre: 'Tessarion',apodo:'la Reina Azul',nacimiento:'120 d.c',muerte:'130 d.c en el Dominio (Ladera)',color:'cobalto',ojos: 'desconocido',genero:'hembra'});
MERGE (n:Dragon {nombre: 'Morghul',nacimiento:'desconocido',muerte:'130 d.c en Desembarco del Rey',color:'desconocido',ojos: 'desconocido',genero:'macho'});
MERGE (n:Dragon {nombre: 'Shrykos',nacimiento:'desconocido',muerte:'130 d.c en Desembarco del Rey',color:'desconocido',ojos: 'desconocido',genero:'hembra'});
MERGE (n:Dragon {nombre: 'Stormcloud',nacimiento:'desconocido',muerte:'130 d.c en Rocadragón',color:'bronze',ojos: 'desconocido',genero:'macho'});
MERGE (n:Dragon {nombre: 'Morning',nacimiento:'129-131 d.c en el Valle de Arryn',muerte:'136-153 d.c',color:'desconocido',ojos: 'desconocido',genero:'macho'});
MERGE (n:Dragon {nombre: 'Sheepstealer',nacimiento:'35 d.c en Dragonstone',muerte:'136-153 dc',color:'café',ojos: 'desconocido',genero:'macho'});
MERGE (n:Dragon {nombre: 'Cannibal',nacimiento:'+/- 114 a.c',muerte:'desconocida',color:'negro',ojos: 'verdes',genero:'macho'});
MERGE (n:Dragon {nombre: 'Grey Ghost',nacimiento:'en Dragonstone',muerte:'130 dc en Rocadragón',color:'gris blanco',ojos: 'desconocido',genero:'macho'});
MERGE (n:Dragon {nombre: 'Viserion',nacimiento:'299 dc en el mar Dothraki',muerte:'vivo',color:'crema y dorado',ojos: 'dorados',genero:'macho'});
MERGE (n:Dragon {nombre: 'Rhaegal',nacimiento:'299 dc en el mar Dothraki',muerte:'vivo',color:'verde y bronce',ojos: 'bronce',genero:'macho'});
MERGE (n:Dragon {nombre: 'Drogon',nacimiento:'299 dc en el mar Dothraki',muerte:'vivo',color:'negro y rojo',ojos: 'rojos',genero:'macho'});






MERGE (start:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (end:Personaje {nombre: 'Alyssa Velaryon'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Rogar Baratheon'})
MERGE (end:Personaje {nombre: 'Alyssa Velaryon'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Maegor Targaryen'})
MERGE (end:Personaje {nombre: 'Ceryse Hightower'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Maegor Targaryen'})
MERGE (end:Personaje {nombre: 'Alys Harroway'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Maegor Targaryen'})
MERGE (end:Personaje {nombre: 'Tyanna of the Tower'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Maegor Targaryen'})
MERGE (end:Personaje {nombre: 'Elinor Costayne'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Maegor Targaryen'})
MERGE (end:Personaje {nombre: 'Jeyne Westerling'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Maegor Targaryen'})
MERGE (end:Personaje {nombre: 'Rhaena I Targaryen'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Rhaena I Targaryen'})
MERGE (end:Personaje {nombre: 'Aegon Targaryen (the Uncrowned)'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Rhaena I Targaryen'})
MERGE (end:Personaje {nombre: 'Androw Farman'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (end:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Aemon Targaryen'})
MERGE (end:Personaje {nombre: 'Jocelyn Baratheon'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Baelon Targaryen'})
MERGE (end:Personaje {nombre: 'Alyssa Targaryen'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Daella Targaryen'})
MERGE (end:Personaje {nombre: 'Rodrik Arryn'})
MERGE (start)-[:Esposos]-(end);



CREATE (a:Grupo {nombre: 'los Negros',descripcion:'Apoyaban el reclamo al trono de Rhaenyra Targaryen'}),
       (b:Personaje {nombre: 'Rhaenyra Targaryen',nacimiento:'97 dc en Rocadragón',muerte:'130 dc en Rocadragón',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Princesa, Reina',apodo:'la Reina por Medio Año, el Encanto del Reino',
                    genero:'femenino'}),
       (c:Personaje {nombre: 'Jacaerys Velaryon',nacimiento:'114 dc',muerte:'130 dc durante la Batalla del Gaznate',
                    ojos:'cafés',cabello:'castaño',
                    titulos:'Principe de Dragonstone',apodo:'Jace',
                    genero:'masculino'}),
       (d:Personaje {nombre: 'Lucerys Velaryon',nacimiento:'115 dc en Rocadragón',muerte:'129 dc en la Bahía de los Naufragios en la costa de Bastión de Tormentas',
                    ojos:'cafés',cabello:'castaño',
                    titulos:'Principe, heredero de Marcaderiva',apodo:'Luke',
                    genero:'masculino'}),
       (e:Personaje {nombre: 'Joffrey Velaryon',nacimiento:'117 dc en Rocadragón',muerte:'130 dc en Desembarco del Rey (Lecho de Pulgas) durante el asalto a Pozo Dragón',
                    ojos:'cafés',cabello:'castaño',
                    titulos:'Principe de Dragonstone',apodo:'Joff',
                    genero:'masculino'}),
       (f:Personaje {nombre: 'Aegon III Targaryen',nacimiento:'120 dc en Rocadragón',muerte:'157 dc en Desembarco del Rey',
                    ojos:'purpura oscuro',cabello:'plateado claro',
                    titulos:'Principe, Rey',apodo:'Aegon el menor',
                    genero:'masculino',reinado:'131-157 dc'}),
       (g:Personaje {nombre: 'Viserys II Targaryen',nacimiento:'122 dc en Rocadragón',muerte:'172 dc en Desembarco del Rey',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Mano del Rey,Rey',
                    genero:'masculino',reinado:'171-172 dc'}),
       (h:Personaje {nombre: 'Alyn Velaryon',nacimiento:'115 dc en Casco, Marcaderiva',muerte:'171-176 dc en altamar',
                    ojos:'morados',cabello:'plateado-dorado',apodo:'Alyn de Casco',
                    titulos:'Señor,maestro de barcos,admiral',
                    genero:'masculino'}),
       (i:Personaje {nombre: 'Baela Targaryen',nacimiento:'116 dc en Pentos',muerte:'136-176 dc',
                    ojos:'morados',cabello:'plateado-dorado',apodo:'Gemela Dragón',
                    titulos:'Señora de Marcaderiva, princesa',
                    genero:'femenino'}),
       (j:Personaje {nombre: 'Rhaena II Targaryen',nacimiento:'116 dc en Pentos',muerte:'desconocida',
                    ojos:'morados',cabello:'plateado-dorado',apodo:'Gemela Dragón',
                    titulos:'Señora, princesa',
                    genero:'femenino'}),
       (k:Personaje {nombre: 'Addam Velaryon',nacimiento:'114 dc en Casco, Marcaderiva',muerte:'130 dc en el Dominio (Batalla de la Ladera)',
                    ojos:'morados',cabello:'plateado',apodo:'Addam de Casco',
                    genero:'masculino'}),
       (l:Personaje {nombre: 'Hugh Hammer',nacimiento:'desconocido en Dragonstone',muerte:'130 dc en el Dominio (Batalla de la Ladera)',
                    ojos:'desconocido',cabello:'desconocido',titulo:'Señor', apodo:'el Traidor',
                    genero:'masculino'}),
       (m:Personaje {nombre: 'Ulf el Blanco',nacimiento:'desconocido',muerte:'130 dc en el Dominio (Batalla de la Ladera)',
                    ojos:'desconocido',cabello:'blanquecino',apodo:'el Traidor',titulo:'Señor',
                    genero:'masculino'}),
       (n:Personaje {nombre: 'Mysaria',nacimiento:'desconocido',muerte:'130 DC en Desembarco del Rey',
                    ojos:'claros',cabello:'desconocido',
                    titulos:'Maestra de los susurros',apodo:'el Gusano Blanco',
                    genero:'femenino'}),
       (o:Personaje {nombre: 'Daemon Targaryen',nacimiento:'81 dc',muerte:'130 dc',
                    ojos:'morados',cabello:'plateado',
                    titulos:'Principe, Comandante de la Guardia de la Ciudad, Maestro de moneda,Maestro de Leyes,Rey de Stepstones y el Mar Angosto, Protector del Reino',
                    apodo:'Principe de la Ciudad, Señor Lecho de Pulgas',
                    genero:'masculino',espada:'Dark Sister'}),
       (p:Personaje {nombre: 'Corlys Velaryon',nacimiento:'53 dc',muerte:'132 dc por fiebre',
                    ojos:'desconocido',cabello:'plateado',
                    titulos:'Señor de Marcaderiva, Maestro de barcos,Mano de la Reina,Señor Regente',apodo:'La Serpiente Marina',
                    genero:'masculino'}),
       (bb:Personaje {nombre: 'Rhaenys II Targaryen',nacimiento:'74 dc',muerte:'129 dc',
                    ojos:'lila',cabello:'negro',apodo:'La Reina que nunca fue',
                    titulos:'Princesa, Señora de Marcaderiva',genero:'femenino'}),
       (q:Personaje {nombre: 'Larra Rogare',nacimiento:'115 dc',muerte:'145 dc',
                    ojos:'lila',cabello:'plateado dorado',apodo:'Larra de Lys',
                    titulos:'Señora',genero:'femenino'}),
       (s:Personaje {nombre: 'Aegon IV Targaryen',nacimiento:'135 dc',muerte:'184 dc',
                    ojos:'morados',cabello:'plateado dorado',apodo:'Aegon el Indigno',
                    titulos:'Principe de Rocadragón,Rey',genero:'masculino',reinado:'172-184 dc'}),
       (t:Personaje {nombre: 'Aemon II Targaryen',nacimiento:'136 dc',muerte:'178-183 dc',
                    ojos:'morados',cabello:'plateado dorado',apodo:'el Caballero Dragón',
                    titulos:'Señor,principe, comandante de la Guardia Real',genero:'masculino'}),
       (u:Personaje {nombre: 'Naerys Targaryen',nacimiento:'138 dc',muerte:'179-184 dc postparto',
                    ojos:'morados',cabello:'plateado dorado',
                    titulos:'princesa, Reina',genero:'femenino'}),
       (v:Personaje {nombre: 'Daenaera Velaryon',nacimiento:'127 dc',muerte:'desconocido',
                    ojos:'azules',cabello:'plateado dorado',
                    titulos:'señora, Reina',genero:'femenino'}),
       (w:Personaje {nombre: 'Daeron I Targaryen',nacimiento:'143 dc',muerte:'161 dc en Dorne',
                    ojos:'morados',cabello:'plateado dorado',apodo:'el Joven Dragón',
                    titulos:'principe, Rey',genero:'masculino',reinado:'157-161 dc',espada:'Blackfyre'}),
       (x:Personaje {nombre: 'Baelor I Targaryen',nacimiento:'127 dc',muerte:'desconocido',
                    ojos:'morados',cabello:'plateado dorado',
                    titulos:'Rey, septón',genero:'masculino',reinado:'161-171 dc'}),
       (y:Personaje {nombre: 'Daena Targaryen',nacimiento:'145 dc',muerte:'171 dc',
                    ojos:'morados',cabello:'plateado dorado',apodo:'Daena la Rebelde',
                    titulos:'princesa, Reina',genero:'femenino'}),
       (z:Personaje {nombre: 'Rhaena III Targaryen',nacimiento:'147 dc',muerte:'+/- 171 dc',
                    ojos:'morados',cabello:'dorado plateado',
                    titulos:'princesa, septa',genero:'femenino'}),
       (aa:Personaje {nombre: 'Elaena Targaryen',nacimiento:'150 dc',muerte:'220 dc',
                    ojos:'lila',cabello:'plateado con una veta dorada en el centro',apodo:'Pincesa Dragón',
                    titulos:'princesa, señora de los Pergaminos',genero:'femenino'}),
       (ab:Personaje {nombre: 'Laena II Velaryon',nacimiento:'134 dc',muerte:'desconocida',
                    genero:'femenino'}),
       (ac:Personaje {nombre: 'Corwyn Corbray',nacimiento:'100 dc',muerte:'135 dc',
                    ojos:'desconocido',cabello:'oscuro',titulo:'Señor, regente',
                    genero:'masculino'}),
       (ad:Personaje {nombre: 'Nettles',nacimiento:'113 dc',muerte:'desconocida',
                    ojos:'cafés',cabello:'negro',
                    genero:'femenino'}),
       (ae:Personaje {nombre: 'Jon Waters',nacimiento:'171-176 dc',muerte:'desconocida',
                    ojos:'morados',cabello:'plateado dorado',titulo:'caballero',
                    genero:'masculino'}),
       (af:Personaje {nombre: 'Jeyne Waters',nacimiento:'171-176 dc',muerte:'desconocida',
                    ojos:'morados',cabello:'plateado dorado',
                    genero:'femenino'}),
       (ag:Personaje {nombre: 'Daemon I Blackfyre',nacimiento:'170 dc',muerte:'196 dc en Prado Hierbarroja',
                    ojos:'morados',cabello:'plateado dorado',apodo:'el Dragón negro',reinado:'196 dc',
                    genero:'masculino',titulos:'señor,principe,caballero,rey',espada:'Blackfyre'}),
       (ah:Personaje {nombre: 'Rohanne de Tyrosh',nacimiento:'172 dc',muerte:'212 dc',
                    ojos:'desconocido',cabello:'desconocido',
                    genero:'femenino',titulo:'señora'}),
       (b)-[:Integrante]->(a),
       (c)-[:Integrante]->(a),
       (d)-[:Integrante]->(a),
       (e)-[:Integrante]->(a),
       (f)-[:Integrante]->(a),
       (g)-[:Integrante]->(a),
       (h)-[:Integrante]->(a),
       (i)-[:Integrante]->(a),
       (j)-[:Integrante]->(a),
       (k)-[:Integrante]->(a),
       (l)-[:Integrante]->(a),
       (o)-[:Integrante]->(a),
       (p)-[:Integrante]->(a),
       (bb)-[:Integrante]->(a),
       (ac)-[:Integrante]->(a),
       (ad)-[:Integrante]->(a),
       (g)-[:Esposos]->(q),
       (g)-[:Padre]->(s),
       (q)-[:Padre]->(s),
       (g)-[:Padre]->(t),
       (q)-[:Padre]->(t),
       (g)-[:Padre]->(u),
       (q)-[:Padre]->(u),
       (i)-[:Hermanos]->(j),
       (s)-[:Hermanos]->(t),
       (s)-[:Hermanos]->(u),
       (t)-[:Hermanos]->(u),
       (s)-[:Esposos]->(u),
       (f)-[:Esposos]->(v),
       (f)-[:Padre]->(w),
       (v)-[:Padre]->(w),
       (f)-[:Padre]->(x),
       (v)-[:Padre]->(x),
       (f)-[:Padre]->(y),
       (v)-[:Padre]->(y),
       (f)-[:Padre]->(z),
       (v)-[:Padre]->(z),
       (f)-[:Padre]->(aa),
       (v)-[:Padre]->(aa),
       (w)-[:Hermanos]->(x),
       (w)-[:Hermanos]->(y),
       (w)-[:Hermanos]->(z),
       (w)-[:Hermanos]->(aa),
       (x)-[:Hermanos]->(y),
       (x)-[:Hermanos]->(z),
       (x)-[:Hermanos]->(aa),
       (y)-[:Hermanos]->(z),
       (y)-[:Hermanos]->(aa),
       (z)-[:Hermanos]->(aa),
       (y)-[:Esposos]->(x),
       (p)-[:Padre]->(h),
       (p)-[:Padre]->(k),
       (h)-[:Hermanos]->(k),
       (h)-[:Esposos]->(i),
       (h)-[:Padre]->(ab),
       (i)-[:Padre]->(ab),
       (h)-[:amorio]->(aa),
       (j)-[:Esposos]->(ac),
       (s)-[:amorio]->(y),
       (aa)-[:Padre]->(ae),
       (h)-[:Padre]->(ae),
       (aa)-[:Padre]->(af),
       (h)-[:Padre]->(af),
       (ae)-[:Hermanos]->(af),
       (s)-[:Padre]->(ag),
       (y)-[:Padre]->(ag),
       (ag)-[:Esposos]->(ah);
       


MERGE (start:casa {nombre: 'casa Arryn'})
MERGE (end:Grupo{nombre: 'los Negros'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:casa {nombre: 'casa Frey'})
MERGE (end:Grupo{nombre: 'los Negros'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:casa {nombre: 'casa Greyjoy'})
MERGE (end:Grupo{nombre: 'los Negros'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:casa {nombre: 'casa Stark'})
MERGE (end:Grupo{nombre: 'los Negros'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:casa {nombre: 'casa Tully'})
MERGE (end:Grupo{nombre: 'los Negros'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:casa {nombre: 'casa Velaryon'})
MERGE (end:Grupo{nombre: 'los Negros'})
MERGE (start)-[:Integrante]->(end);


MERGE (n:Personaje {nombre: 'Viserys I Targaryen',nacimiento:'77 AC',muerte:'129 AC',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Principe de Rocadragón, Rey de los Siete Reinos',
                    genero:'masculino'});


MERGE (start:Personaje {nombre: 'Viserys I Targaryen'})
MERGE (end:Personaje {nombre: 'Daemon Targaryen'})
MERGE (start)-[:Hermanos]-(end);

MERGE (n:Personaje {nombre: 'Laena Velaryon',nacimiento:'92 dc',muerte:'120 dc en Marcaderiva',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Señora',
                    genero:'femenino'});
MERGE (n:Personaje {nombre: 'Laenor Velaryon',nacimiento:'94 dc',muerte:'120 dc en Marcaderiva',
                    ojos:'morados',cabello:'plateado-blanco',
                    titulos:'Señor, principe consorte',
                    genero:'masculino'});

MERGE (start:Personaje {nombre: 'Laena Velaryon'})
MERGE (end:Personaje {nombre: 'Laenor Velaryon'})
MERGE (start)-[:Hermanos]-(end);

MERGE (n:Personaje {nombre: 'Joffrey Lonmouth',nacimiento:'99 dc',muerte:'114 dc en Marcaderiva',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'Señor, caballero',
                    genero:'masculino'});
MERGE (n:Personaje {nombre: 'Harwin Strong',nacimiento:'90 ac',muerte:'120 ac en Harrenhal',
                    ojos:'cafés',cabello:'castaño',
                    titulos:'Señor, Capitan de la Guardia Real de la Ciudad',apodo:'Machacahuesos',
                    genero:'masculino'});

MERGE (start:Personaje {nombre: 'Aemond Targaryen'})
MERGE (end:Personaje {nombre: 'Alys Rivers'})
MERGE (start)-[:Amorio]-(end);


MERGE (start:Personaje {nombre: 'Laenor Velaryon'})
MERGE (end:Personaje {nombre: 'Joffrey Lonmouth'})
MERGE (start)-[:Amorio]-(end);


MERGE (n:Personaje {nombre: 'Aemma Arryn',nacimiento:'82 AC en el Nido de Águilas',muerte:'105 AC en Desembarco del Rey (postparto)',
                    ojos:'morados-azules',cabello:'plateado-dorado',
                    titulos:'Señora, Reina',
                    genero:'femenino'});

MERGE (n:Personaje {nombre: 'Rhea Royce',nacimiento:'desconocido',muerte:'115 AC en el Valle de Arryn (accidente de caballo)',
                    ojos:'cafés (supuestos)',cabello:'castaño (supuesto)',
                    titulos:'Señora de Runestone',
                    genero:'femenino'});
MERGE (n:Personaje {nombre: 'Rodrik Arryn',nacimiento:'44 AC',muerte:'82-97 AC',
                    ojos:'azules (supuestos)',cabello:'negro (supuesto)',
                    titulos:'Señor de Eyrie, Guardián del Este, Maestro de Leyes, Lord Justiciero',
                    genero:'masculino'});




MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:Personaje {nombre: 'Mysaria'})
MERGE (start)-[:amorio]-(end);

MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:Personaje {nombre: 'Rhea Royce'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:Personaje {nombre: 'Laena Velaryon'})
MERGE (start)-[:Esposos]-(end);






CREATE (a:Grupo {nombre: 'los Verdes',descripcion:'Apoyaban el reclamo al trono de Aegon II Targaryen'}),
       (b:Personaje {nombre: 'Aegon II Targaryen',nacimiento:'107 dc en Desembarco del Rey',muerte:'131 dc',
                    ojos:'morados',cabello:'plateado-dorado',espada:'Blackfyre',
                    titulos:'Principe, Rey',apodo:'Aegon el Mayor, Aegon el Usurpador',
                    genero:'masculino',reinado:'129-131 ac'}),
       (c:Personaje {nombre: 'Alicent Hightower',nacimiento:'88 dc',muerte:'133 dc por fiebre',
                    ojos:'desconocido',cabello:'castaño',
                    titulos:'Señora, Reina, Reina Viuda',
                    genero:'femenino'}),
       (d:Personaje {nombre: 'Helaena Targaryen',nacimiento:'109 dc',muerte:'130 dc suicidio',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Princesa, Reina',
                    genero:'femenino'}),
       (e:Personaje {nombre: 'Jaehaerys Targaryen',nacimiento:'123 dc',muerte:'129 dc',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Principe',
                    genero:'masculino'}),
       (f:Personaje {nombre: 'Jaehaera Targaryen',nacimiento:'123 dc',muerte:'133 dc suicidio',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Princesa, Reina',
                    genero:'femenino'}),
       (g:Personaje {nombre: 'Maelor Targaryen',nacimiento:'127 dc ',muerte:'130 dc',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Principe',
                    genero:'masculino'}),
       (h:Personaje {nombre: 'Aemond Targaryen',nacimiento:'110 dc',muerte:'130 dc en Ojo de Dioses',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Principe, principe regente',apodo:'Aemond un ojo',
                    genero:'masculino'}),
       (i:Personaje {nombre: 'Daeron Targaryen',nacimiento:'114 dc',muerte:'130 dc en batalla',
                    ojos:'morados',cabello:'plateado-dorado',
                    titulos:'Principe, señor',
                    genero:'masculino'}),
       (j:Personaje {nombre: 'Alys Rivers',nacimiento:'89 AC',muerte:'desconocida',
                    ojos:'desconocido',cabello:'negro',apodo:'la Reina Bruja',
                    genero:'femenino'}),
       (k:Personaje {nombre: 'Hugh Hammer',nacimiento:'desconocido en Dragonstone',muerte:'130 dc en el Dominio (Batalla de la Ladera)',
                    ojos:'desconocido',cabello:'desconocido',titulo:'Señor', apodo:'el Traidor',
                    genero:'masculino'}),
       (l:Personaje {nombre: 'Ulf el Blanco',nacimiento:'desconocido',muerte:'130 dc en el Dominio (Batalla de la Ladera)',
                    ojos:'desconocido',cabello:'blanquecino',apodo:'el Traidor',titulo:'Señor',
                    genero:'masculino'}),
       (m:Personaje {nombre: 'Otto Hightower',nacimiento:'76 dc',muerte:'130 dc',
                    ojos:'desconocido',cabello:'oscuro',apodo:'el Traidor',titulo:'Señor,mano del Rey',
                    genero:'masculino'}),
       (n:Personaje {nombre: 'Criston Cole',nacimiento:'82 dc',muerte:'130 dc en batalla',
                    ojos:'verdes',cabello:'negro',apodo:'el Hacedor de Reyes',titulo:'Señor,mano del Rey,comandante de la guardia Real',
                    genero:'masculino'}),
       
       (p:Personaje {nombre: 'Garmund Hightower',nacimiento:'116-124 dc',muerte:'desconocida',
                    ojos:'claros',cabello:'oscuro',titulo:'Señor',
                    genero:'masculino'}),
       (q:Personaje {nombre: 'Gwayne Hightower',nacimiento:'96 dc',muerte:'130 dc',
                    ojos:'desconocido',cabello:'oscuro',titulo:'Señor',
                    genero:'masculino'}),
       (b)-[:Integrante]->(a),
       (c)-[:Integrante]->(a),
       (d)-[:Integrante]->(a),
       (d)-[:Integrante]->(a),
       (e)-[:Integrante]->(a),
       (f)-[:Integrante]->(a),
       (g)-[:Integrante]->(a),
       (h)-[:Integrante]->(a),
       (i)-[:Integrante]->(a),
       (j)-[:Integrante]->(a),
       (k)-[:Integrante]->(a),
       (l)-[:Integrante]->(a),
       (m)-[:Integrante]->(a),
       (n)-[:Integrante]->(a),
       (p)-[:Integrante]->(a),
       (q)-[:Integrante]->(a),
       (m)-[:Padre]->(c),
       (m)-[:Padre]->(q),
       (c)-[:Hermanos]->(q),
       (e)-[:Hermanos]->(f),
       (e)-[:Hermanos]->(g),
       (f)-[:Hermanos]->(g),

MERGE (start:casa {nombre: 'casa Baratheon'})
MERGE (end:Grupo{nombre: 'los Verdes'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:casa {nombre: 'casa Hightower'})
MERGE (end:Grupo{nombre: 'los Verdes'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:casa {nombre: 'casa Lannister'})
MERGE (end:Grupo{nombre: 'los Verdes'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:casa {nombre: 'casa Velaryon'})
MERGE (end:Grupo{nombre: 'los Verdes'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:casa {nombre: 'casa Tully'})
MERGE (end:Grupo{nombre: 'los Verdes'})
MERGE (start)-[:Integrante]->(end);

MERGE(a:Grupo {nombre: 'Triarquia',cuando:'96-131 dc'})

MERGE (start:Grupo {nombre: 'Triarquia'})
MERGE (end:Grupo{nombre: 'los Verdes'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:ciudad {nombre: 'Myr'})
MERGE (end:Grupo{nombre: 'Triarquia'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:ciudad {nombre: 'Lys'})
MERGE (end:Grupo{nombre: 'Triarquia'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:ciudad {nombre: 'Tyrosh'})
MERGE (end:Grupo{nombre: 'Triarquia'})
MERGE (start)-[:Integrante]->(end);


MERGE (start:Personaje {nombre: 'Aemon Targaryen'})
MERGE (end:Personaje {nombre: 'Rhaenys II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Jocelyn Baratheon'})
MERGE (end:Personaje {nombre: 'Rhaenys II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Baelon Targaryen'})
MERGE (end:Personaje {nombre: 'Viserys I Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Targaryen'})
MERGE (end:Personaje {nombre: 'Viserys I Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Baelon Targaryen'})
MERGE (end:Personaje {nombre: 'Daemon Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Targaryen'})
MERGE (end:Personaje {nombre: 'Daemon Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Corlys Velaryon'})
MERGE (end:Personaje {nombre: 'Laena Velaryon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys II Targaryen'})
MERGE (end:Personaje {nombre: 'Laena Velaryon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Corlys Velaryon'})
MERGE (end:Personaje {nombre: 'Laenor Velaryon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys II Targaryen'})
MERGE (end:Personaje {nombre: 'Laenor Velaryon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rodrik Arryn'})
MERGE (end:Personaje {nombre: 'Aemma Arryn'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Daella Targaryen'})
MERGE (end:Personaje {nombre: 'Aemma Arryn'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Viserys I Targaryen'})
MERGE (end:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aemma Arryn'})
MERGE (end:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:Personaje {nombre: 'Rhaena II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Laena Velaryon'})
MERGE (end:Personaje {nombre: 'Rhaena II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:Personaje {nombre: 'Baela Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Laena Velaryon'})
MERGE (end:Personaje {nombre: 'Baela Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:Personaje {nombre: 'Aegon III Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (end:Personaje {nombre: 'Aegon III Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:Personaje {nombre: 'Viserys II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (end:Personaje {nombre: 'Viserys II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Laenor Velaryon'})
MERGE (end:Personaje {nombre: 'Jacaerys Velaryon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (end:Personaje {nombre: 'Jacaerys Velaryon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Laenor Velaryon'})
MERGE (end:Personaje {nombre: 'Lucerys Velaryon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (end:Personaje {nombre: 'Lucerys Velaryon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Laenor Velaryon'})
MERGE (end:Personaje {nombre: 'Joffrey Velaryon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (end:Personaje {nombre: 'Joffrey Velaryon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Lucerys Targaryen'})
MERGE (end:Personaje {nombre: 'Joffrey Velaryon'})
MERGE (start)-[:Hermanos]->(end);

MERGE (start:Personaje {nombre: 'Lucerys Targaryen'})
MERGE (end:Personaje {nombre: 'Jacaerys Velaryon'})
MERGE (start)-[:Hermanos]->(end);

MERGE (start:Personaje {nombre: 'Joffrey Targaryen'})
MERGE (end:Personaje {nombre: 'Jacaerys Velaryon'})
MERGE (start)-[:Hermanos]->(end);


MERGE (start:Personaje {nombre: 'Viserys I Targaryen'})
MERGE (end:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alicent Targaryen'})
MERGE (end:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Viserys I Targaryen'})
MERGE (end:Personaje {nombre: 'Aemond Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alicent Targaryen'})
MERGE (end:Personaje {nombre: 'Aemond Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Viserys I Targaryen'})
MERGE (end:Personaje {nombre: 'Helaena Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alicent Targaryen'})
MERGE (end:Personaje {nombre: 'Helaena Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Viserys I Targaryen'})
MERGE (end:Personaje {nombre: 'Daeron Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alicent Targaryen'})
MERGE (end:Personaje {nombre: 'Daeron Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (end:Personaje {nombre: 'Jaehaerys Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Helaena Targaryen'})
MERGE (end:Personaje {nombre: 'Jaehaerys Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (end:Personaje {nombre: 'Jaehaera Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Helaena Targaryen'})
MERGE (end:Personaje {nombre: 'Jaehaera Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (end:Personaje {nombre: 'Maelor Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Helaena Targaryen'})
MERGE (end:Personaje {nombre: 'Maelor Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Garmund Hightower'})
MERGE (end:Personaje{nombre: 'Rhaena II Targaryen'})
MERGE (start)-[:Esposos]-(end);


MERGE (start:Personaje {nombre: 'Rhaenys II Targaryen'})
MERGE (end:Personaje {nombre: 'Corlys Baratheon'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Viserys I Targaryen'})
MERGE (end:Personaje {nombre: 'Aemma Arryn'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Viserys I Targaryen'})
MERGE (end:Personaje {nombre: 'Alicent Hightower'})
MERGE (start)-[:Esposos]-(end);


MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (end:Personaje {nombre: 'Laenor Velaryon'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Joffrey Lonmouth'})
MERGE (end:Personaje {nombre: 'Laenor Velaryon'})
MERGE (start)-[:Amorio]-(end);

MERGE (start:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (end:Personaje {nombre: 'Harwin Strong'})
MERGE (start)-[:Amorio]-(end);

MERGE (start:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (end:Personaje {nombre: 'Helaena Targaryen'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (end:Personaje {nombre: 'Helaena Targaryen'})
MERGE (start)-[:Hermanos]-(end);

MERGE (start:Personaje {nombre: 'Aemond Targaryen'})
MERGE (end:Personaje {nombre: 'Helaena Targaryen'})
MERGE (start)-[:Hermanos]-(end);

MERGE (start:Personaje {nombre: 'Daeron Targaryen'})
MERGE (end:Personaje {nombre: 'Helaena Targaryen'})
MERGE (start)-[:Hermanos]-(end);

MERGE (start:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (end:Personaje {nombre: 'Aemond Targaryen'})
MERGE (start)-[:Hermanos]-(end);

MERGE (start:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (end:Personaje {nombre: 'Daeron Targaryen'})
MERGE (start)-[:Hermanos]-(end);

MERGE (start:Personaje {nombre: 'Daeron Targaryen'})
MERGE (end:Personaje {nombre: 'Aemond Targaryen'})
MERGE (start)-[:Hermanos]-(end);

MERGE (start:Personaje {nombre: 'Aegon III Targaryen'})
MERGE (end:Personaje {nombre: 'Jaehaera Targaryen'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Aegon III Targaryen'})
MERGE (end:Personaje {nombre: 'Danaera Velaryon'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Rhaena II Targaryen'})
MERGE (end:Personaje {nombre: 'Corwyn Corbray'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Rhaena II Targaryen'})
MERGE (end:Personaje {nombre: 'Garmund Hightower'})
MERGE (start)-[:Esposos]-(end);


MERGE (start:Personaje {nombre: 'Aegon I Targaryen'})
MERGE (end:Grupo {nombre: 'Los Conquistadores'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:Personaje {nombre: 'Visenya Targaryen'})
MERGE (end:Grupo {nombre: 'Los Conquistadores'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys I Targaryen'})
MERGE (end:Grupo {nombre: 'Los Conquistadores'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:Personaje {nombre: 'Maegor Targaryen'})
MERGE (end:Grupo {nombre: 'Los Hijos y Nietos del Dragón'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (end:Grupo {nombre: 'Los Hijos y Nietos del Dragón'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:Personaje {nombre: 'Rhaena I Targaryen'})
MERGE (end:Grupo {nombre: 'Los Hijos y Nietos del Dragón'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:Personaje {nombre: 'Aegon Targaryen (the Uncrowned)'})
MERGE (end:Grupo {nombre: 'Los Hijos y Nietos del Dragón'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:Personaje {nombre: 'Viserys Targaryen'})
MERGE (end:Grupo {nombre: 'Los Hijos y Nietos del Dragón'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (end:Grupo {nombre: 'Los Hijos y Nietos del Dragón'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (end:Grupo {nombre: 'Los Hijos y Nietos del Dragón'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:Personaje {nombre: 'Vaella Targaryen'})
MERGE (end:Grupo {nombre: 'Los Hijos y Nietos del Dragón'})
MERGE (start)-[:Integrante]->(end);

MERGE (start:Personaje {nombre: 'Elinor Costayne'})
MERGE (end:Grupo {nombre: 'Black Brides'})
MERGE (start)-[:Integrante]-(end);

MERGE (start:Personaje {nombre: 'Jeyne Westerling'})
MERGE (end:Grupo {nombre: 'Black Brides'})
MERGE (start)-[:Integrante]-(end);

MERGE (start:Personaje {nombre: 'Rhaena I Targaryen'})
MERGE (end:Grupo {nombre: 'Black Brides'})
MERGE (start)-[:Integrante]-(end);


MERGE (start:Personaje {nombre: 'Aegon I Targaryen'})
MERGE (end:Personaje {nombre: 'Maegor Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon I Targaryen'})
MERGE (end:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Visenya Targaryen'})
MERGE (end:Personaje {nombre: 'Maegor Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys I Targaryen'})
MERGE (end:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (end:Personaje {nombre: 'Rhaena I Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Velaryon'})
MERGE (end:Personaje {nombre: 'Rhaena I Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (end:Personaje {nombre: 'Aegon Targaryen (the Uncrowned)'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Velaryon'})
MERGE (end:Personaje {nombre: 'Aegon Targaryen (the Uncrowned)'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (end:Personaje {nombre: 'Viserys Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Velaryon'})
MERGE (end:Personaje {nombre: 'Viserys Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (end:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Velaryon'})
MERGE (end:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (end:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Velaryon'})
MERGE (end:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (end:Personaje {nombre: 'Vaella Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Velaryon'})
MERGE (end:Personaje {nombre: 'Vaella Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rogar Baratheon'})
MERGE (end:Personaje {nombre: 'Jocelyn Baratheon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Velaryon'})
MERGE (end:Personaje {nombre: 'Jocelyn Baratheon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rogar Baratheon'})
MERGE (end:Personaje {nombre: 'Boremund Baratheon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Velaryon'})
MERGE (end:Personaje {nombre: 'Boremund Baratheon'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon Targaryen (the Uncrowned)'})
MERGE (end:Personaje {nombre: 'Aerea Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rhaena I Targaryen'})
MERGE (end:Personaje {nombre: 'Aerea Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon Targaryen (the Uncrowned)'})
MERGE (end:Personaje {nombre: 'Rhaella I Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Rhaena I Targaryen'})
MERGE (end:Personaje {nombre: 'Rhaella I Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (end:Personaje {nombre: 'Aemon Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (end:Personaje {nombre: 'Aemon Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (end:Personaje {nombre: 'Baelon Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (end:Personaje {nombre: 'Baelon Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (end:Personaje {nombre: 'Alyssa Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (end:Personaje {nombre: 'Alyssa Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (end:Personaje {nombre: 'Maegelle Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (end:Personaje {nombre: 'Maegelle Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (end:Personaje {nombre: 'Vaegon Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (end:Personaje {nombre: 'Vaegon Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (end:Personaje {nombre: 'Daella Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (end:Personaje {nombre: 'Daella Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (end:Personaje {nombre: 'Saera Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (end:Personaje {nombre: 'Saera Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (end:Personaje {nombre: 'Viserra Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (end:Personaje {nombre: 'Viserra Targaryen'})
MERGE (start)-[:Padre]->(end);


CREATE (a:Personaje {nombre: 'Michael Manwoody',nacimiento:'desconcocido',muerte:'desconocido',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'caballero',
                    genero:'masculino'}),
       (b:Personaje {nombre: 'Ossifer Plumm',nacimiento:'desconocido',muerte:'176 dc',
                    ojos:'desconocido',cabello:'desconocidoo',
                    titulos:'Señor',
                    genero:'masculino'}),
       (c:Personaje {nombre: 'Ronnel Penrose',nacimiento:'desconocido',muerte:'188-209 dc',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'Señor de los Pergaminos, Maestro de moneda',
                    genero:'masculino'}),
       (d:Personaje {nombre: 'Viserys Plumm',nacimiento:'176 dc',muerte:'212 dc',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'Señor',
                    genero:'masculino'}),
       (e:Personaje {nombre: 'Robin Penrose',nacimiento:'184-197 dc',muerte:'desconocida',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'Señor',
                    genero:'masculino'}),
       (f:Personaje {nombre: 'Laena Penrose',nacimiento:'185-198 dc',muerte:'desconocida',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'Señora',
                    genero:'femenino'}),
       (g:Personaje {nombre: 'Jocelyn Penrose',nacimiento:'186-199 dc',muerte:'desconocida',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'Señora',
                    genero:'femenino'}),
       (h:Personaje {nombre: 'Joy Penrose',nacimiento:'186-200 dc',muerte:'desconocida',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'Señora',
                    genero:'femenino'}),
       (i:Personaje {nombre: 'Daeron II Targaryen',nacimiento:'153 dc',muerte:'209 dc',
                    ojos:'morados',cabello:'plateado dorado',reinado:'184-209 dc',
                    titulos:'principe, Rey',apodo:'Daeron el Bueno',
                    genero:'masculino'}),
       (j:Personaje {nombre: 'Daenerys I Targaryen',nacimiento:'172 dc',muerte:'desconocido',
                    ojos:'morados',cabello:'plateado dorado',
                    titulos:'princesa, princesa consorte de Dorne',apodo:'la primera Daenerys',
                    genero:'femenino'}),
       (k:Personaje {nombre: 'Maron Martell',nacimiento:'147-158 dc',muerte:'desconocido',
                    ojos:'oscuros',cabello:'oscuros',
                    titulos:'principe de Dorne, señor de lanza de sol',
                    genero:'masculino'}),
       (l:Personaje {nombre: 'Myriah Martell',nacimiento:'146-158 dc',muerte:'184 dc',
                    ojos:'oscuros',cabello:'castaño',
                    titulos:'princesa, Reina',
                    genero:'femenino'}),
       (m:Personaje {nombre: 'Baelor Targaryen',nacimiento:'170 dc',muerte:'209 dc durante un torneo en el Dominio',
                    ojos:'oscuros',cabello:'castaño',apodo:'Baelor el Rompelanzas',
                    titulos:'principe, mano del rey',
                    genero:'masculino'}),
       (n:Personaje {nombre: 'Jena Dondarrion',nacimiento:'desconocido',muerte:'+/- 183 dc',
                    ojos:'azules',cabello:'desconocido',
                    titulos:'señora',
                    genero:'femenino'}),
       (o:Personaje {nombre: 'Valarr Targaryen',nacimiento:'182-193 dc',muerte:'209 dc',
                    ojos:'azules',cabello:'castaño con una mecha plateada dorada',
                    titulos:'principe, señor, mano del rey',apodo:'el Principe Joven',
                    genero:'masculino'}),
       (p:Personaje {nombre: 'Matarys Targaryen',nacimiento:'183-209 dc',muerte:'209 dc',
                    ojos:'azules',cabello:'castaño',
                    titulos:'principe',apodo:'el Principe aun más Joven',
                    genero:'masculino'}),
       (q:Personaje {nombre: 'Kiera de Tyrosh',nacimiento:'desconocido',muerte:'desconocido',
                    titulos:'señora',
                    genero:'femenino'}),
       (r:Personaje {nombre: 'Aerys II Targaryen',nacimiento:'172-177 dc',muerte:'221 dc',
                    titulos:'Rey',reinado:'209-221 dc',
                    genero:'masculino'}),
       (s:Personaje {nombre: 'Aelinor Penrose',nacimiento:'desconocido',muerte:'desconocido',
                    titulos:'Señora, Reina',
                    genero:'femenino'}),
       (t:Personaje {nombre: 'Rhaegel Targaryen',nacimiento:'173-178 dc',muerte:'215 dc',
                    titulos:'Principe',
                    genero:'masculino'}),
       (u:Personaje {nombre: 'Alys Arryn',nacimiento:'desconocido',muerte:'desconocido',
                    titulos:'Señora',
                    genero:'femenino'}),
       (v:Personaje {nombre: 'Aelor Targaryen',nacimiento:'195-211 dc',muerte:'217 dc',
                    titulos:'principe',
                    genero:'masculino'}),
       (w:Personaje {nombre: 'Aelora Targaryen',nacimiento:'195-211 dc',muerte:'217-221 dc',
                    titulos:'princesa',
                    genero:'femenino'}),
       
       (x:Personaje {nombre: 'Daenora Targaryen',nacimiento:'212-216 dc',muerte:'desconocido',
                    titulos:'princesa',
                    genero:'femenino'}),
       (y:Personaje {nombre: 'Maekar I Targaryen',nacimiento:'174-179 dc',muerte:'233 dc en batalla',
                    titulos:'principe, Rey', reinado:'221-233 dc',apodo:'el Yunque',
                    genero:'masculino',ojos:'morados',cabella:'rubio palido'}),
       (z:Personaje {nombre: 'Dyanna Dayne',nacimiento:'149-179 dc',muerte:'201-209 dc',
                    titulos:'señora',
                    genero:'femenino'}),
       
       (b)-[:Padre]->(d),
       (c)-[:Padre]->(e),
       (c)-[:Padre]->(f),
       (c)-[:Padre]->(g),
       (c)-[:Padre]->(h),
       (e)-[:Hermanos]->(f),
       (e)-[:Hermanos]->(g),
       (e)-[:Hermanos]->(h),
       (f)-[:Hermanos]->(g),
       (f)-[:Hermanos]->(h),
       (g)-[:Hermanos]->(h),
       (i)-[:Hermanos]->(j),
       (k)-[:Esposos]->(j),
       (l)-[:Esposos]->(i),
       (i)-[:Padre]->(m),
       (l)-[:Padre]->(m),
       (m)-[:Esposos]->(n),
       (m)-[:Padre]->(o),
       (n)-[:Padre]->(o),
       (m)-[:Padre]->(p),
       (n)-[:Padre]->(p),
       (o)-[:Hermanos]->(p),
       (o)-[:Esposos]->(q),
       (i)-[:Padre]->(r),
       (l)-[:Padre]->(r),
       (r)-[:Esposos]->(s),
       (i)-[:Padre]->(t),
       (l)-[:Padre]->(t),
       (t)-[:Esposos]->(u),
       (v)-[:Esposos]->(w),
       (t)-[:Padre]->(v),
       (u)-[:Padre]->(v),
       (t)-[:Padre]->(w),
       (u)-[:Padre]->(w),
       (t)-[:Padre]->(x),
       (u)-[:Padre]->(x),
       (v)-[:Hermanos]->(w),
       (v)-[:Hermanos]->(x),
       (w)-[:Hermanos]->(x),
       (i)-[:Padre]->(y),
       (l)-[:Padre]->(y),
       (m)-[:Hermanos]->(r),
       (m)-[:Hermanos]->(t),
       (m)-[:Hermanos]->(y),
       (r)-[:Hermanos]->(t),
       (r)-[:Hermanos]->(y),
       (t)-[:Hermanos]->(y),
       (y)-[:Esposos]->(z);

MERGE (start:Personaje {nombre: 'Michael Manwoody'})
MERGE (end:Personaje{nombre: 'Elaena Targaryen'})
MERGE (start)-[:Esposos]->(end);

MERGE (start:Personaje {nombre: 'Ossifer Plumm'})
MERGE (end:Personaje{nombre: 'Elaena Targaryen'})
MERGE (start)-[:Esposos]->(end);

MERGE (start:Personaje {nombre: 'Ronnel Penrose'})
MERGE (end:Personaje{nombre: 'Elaena Targaryen'})
MERGE (start)-[:Esposos]->(end);

MERGE (start:Personaje {nombre: 'Elaena Targaryen'})
MERGE (end:Personaje{nombre: 'Viserys Plumm'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Elaena Targaryen'})
MERGE (end:Personaje{nombre: 'Robin Penrose'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Elaena Targaryen'})
MERGE (end:Personaje{nombre: 'Laena Penrose'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Elaena Targaryen'})
MERGE (end:Personaje{nombre: 'Jocelyn Penrose'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Elaena Targaryen'})
MERGE (end:Personaje{nombre: 'Joy Penrose'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Daeron II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Naerys Targaryen'})
MERGE (end:Personaje{nombre: 'Daeron II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Daenerys I Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Naerys Targaryen'})
MERGE (end:Personaje{nombre: 'Daenerys I Targaryen'})
MERGE (start)-[:Padre]->(end);

CREATE (a:Personaje {nombre: 'Daeron (el Borracho)',nacimiento:'190-191 dc',muerte:'221-233 dc',
                    ojos:'desconocido',cabello:'castaño',
                    titulos:'principe',
                    genero:'masculino'}),
       (b:Personaje {nombre: 'Vaella II Targaryen',nacimiento:'222 dc',muerte:'desconocido',
                    ojos:'desconocido',cabello:'castaño',
                    titulos:'princesa',
                    genero:'femenino'}),
       (c:Personaje {nombre: 'Aerion III Targaryen',nacimiento:'191-194 dc',muerte:'232 dc',
                    ojos:'morado',cabello:'plateado-dorado',alias:'Aerion el Monstruoso',
                    titulos:'principe',
                    genero:'masculino'}),
       (d:Personaje {nombre: 'Maegor II Targaryen',nacimiento:'232 dc',muerte:'desconocido',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'principe',
                    genero:'masculino'}),
       (e:Personaje {nombre: 'Aemon III Targaryen',nacimiento:'198 dc',muerte:'300 dc',
                    ojos:'desconocido',cabello:'plateado',
                    titulos:'principe, Maestre de la Guardia de la Noche',
                    genero:'masculino'}),
       (f:Personaje {nombre: 'Daella II Targaryen',nacimiento:'199 dc',muerte:'desconocido',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'princesa',
                    genero:'femenino'}),
       (g:Personaje {nombre: 'Rhae Targaryen',nacimiento:'201-209 dc',muerte:'desconocido',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'princesa',
                    genero:'femenino'}),
       (h:Personaje {nombre: 'Aegon V Targaryen',nacimiento:'200 dc',muerte:'259 dc',
                    ojos:'morados',cabello:'plateado dorado',
                    titulos:'principe, Rey',reinado:'233-259 dc',
                    genero:'masculino',apodo:'Aegon el Improbable, Egg'}),
       (i:Personaje {nombre: 'Betha Blackwood',nacimiento:'201 dc',muerte:'239 dc',
                    ojos:'negros',cabello:'negro',
                    titulos:'señora, reina',
                    genero:'femenino'}),
       (j:Personaje {nombre: 'Duncan Targaryen',nacimiento:'220-224 dc',muerte:'259 dc',
                    ojos:'desconocido',cabello:'negro',
                    titulos:'principe',apodo:'el Principe de las Libelulas',
                    genero:'masculino'}),
       (k:Personaje {nombre: 'Jaehaerys II Targaryen',nacimiento:'225 dc',muerte:'262 dc',
                    ojos:'morados',cabello:'desconocido',
                    titulos:'principe,rey',reinado:'259-262 dc',
                    genero:'masculino'}),
       (l:Personaje {nombre: 'Shaera Targaryen',nacimiento:'226 dc',muerte:'259 dc',
                    ojos:'morados',cabello:'desconocido',
                    titulos:'princesa,reina',
                    genero:'femenino'}),
       (m:Personaje {nombre: 'Daeron IV Targaryen',nacimiento:'228 dc',muerte:'251 dc',
                    ojos:'desconocido',cabello:'plateado dorado',
                    titulos:'principe',
                    genero:'masculino'}),
       (n:Personaje {nombre: 'Rhaelle Targaryen',nacimiento:'229-234 dc',muerte:'246 dc',
                    ojos:'desconocido',cabello:'plateado dorado',
                    titulos:'princesa, señora',
                    genero:'femenino'}),
       (o:Personaje {nombre: 'Jeremy Norridge',nacimiento:'desconocido',muerte:'251 dc',
                    ojos:'desconocido',cabello:'desconocido',
                    titulos:'señor',
                    genero:'masculino'}),
       (p:Personaje {nombre: 'Aerys II Targaryen',nacimiento:'244 dc',muerte:'283 dc',
                    ojos:'morados',cabello:'plateado dorado',apodo:'el Rey Loco',
                    titulos:'Principe, Rey',reinado:'262-283 dc',
                    genero:'masculino'}),
       (q:Personaje {nombre: 'Rhaella II Targaryen',nacimiento:'245-247 dc',muerte:'284 dc',
                    ojos:'desconocido',cabello:'plateado dorado',
                    titulos:'Princesa, Reina',
                    genero:'femenino'}),
       (r:Personaje {nombre: 'Rhaegar Targaryen',nacimiento:'259 dc',muerte:'283 dc',
                    ojos:'morados',cabello:'plateado dorado',
                    titulos:'Principe',apodo:'el Principe Dragón, el último dragón',
                    genero:'masculino'}),
       (s:Personaje {nombre: 'Elia Martell',nacimiento:'256-257 dc',muerte:'283 dc',
                    ojos:'negros',cabello:'oscuro',
                    titulos:'Princesa, señora',
                    genero:'femenino'}),
       (t:Personaje {nombre: 'Rhaenys III Targaryen',nacimiento:'280 dc',muerte:'283 dc',
                    ojos:'desconocido',cabello:'oscuro',
                    titulos:'Princesa',
                    genero:'femenino'}),
       (u:Personaje {nombre: 'Aegon VI Targaryen',nacimiento:'281 dc',muerte:'vivo',
                    ojos:'desconocido',cabello:'plateado dorado',
                    titulos:'Principe',
                    genero:'masculino'}),
       (v:Personaje {nombre: 'Viserys III Targaryen',nacimiento:'276 dc',muerte:'298 dc en Essos',
                    ojos:'lilas',cabello:'plateado dorado',
                    titulos:'Principe',apodo:'el Rey Mendigo',
                    genero:'masculino'}),
       (w:Personaje {nombre: 'Daenerys II Targaryen',nacimiento:'284 dc',muerte:'viva',
                    ojos:'morados',cabello:'plateado dorado',reinado:'289 dc- actualidad',
                    titulos:'Princesa, Khalessi, Reina de Meeren',apodo:'Dany, Daenerys Stormborn, Madre de Dragones',
                    genero:'femenino'}),
       (x:Personaje {nombre: 'Drogo',nacimiento:'267 dc',muerte:'298 dc',
                    ojos:'negros',cabello:'negros',
                    titulos:'Khal',
                    genero:'masculino'}),
       (y:Personaje {nombre: 'Rhaego',nacimiento:'298-299 dc',muerte:'298-299 dc',
                    ojos:'morados',cabello:'plateado dorado',
                    genero:'masculino'}),
       (z:Personaje {nombre: 'Hizdahr zo Loraq',nacimiento:'en Mereen',muerte:'vivo',
                    ojos:'desconocido',cabello:'rojizo negro',
                    genero:'masculino'}),
       (a)-[:Padre]->(b),
       (c)-[:Padre]->(d),
       (a)-[:Hermanos]->(e),
       (a)-[:Hermanos]->(f),
       (a)-[:Hermanos]->(c),
       (a)-[:Hermanos]->(g),
       (a)-[:Hermanos]->(h),
       (e)-[:Hermanos]->(f),
       (e)-[:Hermanos]->(c),
       (e)-[:Hermanos]->(g),
       (e)-[:Hermanos]->(h),
       (f)-[:Hermanos]->(c),
       (f)-[:Hermanos]->(g),
       (f)-[:Hermanos]->(h),
       (c)-[:Hermanos]->(g),
       (c)-[:Hermanos]->(h),
       (g)-[:Hermanos]->(h),
       (g)-[:Esposos]->(h),
       (h)-[:Padre]->(j),
       (i)-[:Padre]->(j),
       (h)-[:Padre]->(k),
       (i)-[:Padre]->(k),
       (h)-[:Padre]->(l),
       (i)-[:Padre]->(l),
       (h)-[:Padre]->(m),
       (i)-[:Padre]->(m),
       (h)-[:Padre]->(n),
       (i)-[:Padre]->(n),
       (j)-[:Hermanos]->(k),
       (j)-[:Hermanos]->(l),
       (j)-[:Hermanos]->(m),
       (j)-[:Hermanos]->(n),
       (k)-[:Hermanos]->(l),
       (k)-[:Hermanos]->(m),
       (k)-[:Hermanos]->(n),
       (l)-[:Hermanos]->(m),
       (l)-[:Hermanos]->(n),
       (m)-[:Hermanos]->(n),
       (k)-[:Esposos]->(l),
       (m)-[:amorio]->(o),
       (k)-[:Padre]->(p),
       (l)-[:Padre]->(p),
       (k)-[:Padre]->(q),
       (l)-[:Padre]->(q),
       (p)-[:Esposos]->(q),
       (r)-[:Esposos]->(s),
       (r)-[:Padre]->(t),
       (s)-[:Padre]->(t),
       (r)-[:Padre]->(u),
       (s)-[:Padre]->(u),
       (t)-[:Hermanos]->(u),
       (p)-[:Padre]->(r),
       (q)-[:Padre]->(r),
       (p)-[:Padre]->(v),
       (q)-[:Padre]->(v),
       (p)-[:Padre]->(w),
       (q)-[:Padre]->(w),
       (r)-[:Hermanos]->(v),
       (r)-[:Hermanos]->(w),
       (v)-[:Hermanos]->(w),
       (w)-[:Esposos]->(x),
       (w)-[:Padre]->(y),
       (x)-[:Padre]->(y),
       (w)-[:Esposos]->(z);
       
MERGE (start:Personaje {nombre: 'Daenora Targaryen'})
MERGE (end:Personaje{nombre: 'Aerion III Targaryen'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Daenora Targaryen'})
MERGE (end:Personaje{nombre: 'Maegor II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Kiera de Tyrosh'})
MERGE (end:Personaje{nombre: 'Daeron Targaryen (el Borracho)'})
MERGE (start)-[:Esposos]-(end);

MERGE (start:Personaje {nombre: 'Kiera de Tyrosh'})
MERGE (end:Personaje{nombre: 'Vaella II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Daeron Targaryen (el Borracho)'})
MERGE (end:Personaje{nombre: 'Vaella II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Maekar I Targaryen'})
MERGE (end:Personaje{nombre: 'Daeron Targaryen (el Borracho)'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Dyanna Dayne'})
MERGE (end:Personaje{nombre: 'Daeron Targaryen (el Borracho)'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Maekar I Targaryen'})
MERGE (end:Personaje{nombre: 'Aerion II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Dyanna Dayne'})
MERGE (end:Personaje{nombre: 'Aerion II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Maekar I Targaryen'})
MERGE (end:Personaje{nombre: 'Aemon III Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Dyanna Dayne'})
MERGE (end:Personaje{nombre: 'Aemon III Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Maekar I Targaryen'})
MERGE (end:Personaje{nombre: 'Daella II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Dyanna Dayne'})
MERGE (end:Personaje{nombre: 'Daella II Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Maekar I Targaryen'})
MERGE (end:Personaje{nombre: 'Aegon V Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Dyanna Dayne'})
MERGE (end:Personaje{nombre: 'Aegon V Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Maekar I Targaryen'})
MERGE (end:Personaje{nombre: 'Rhae Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Dyanna Dayne'})
MERGE (end:Personaje{nombre: 'Rhae Targaryen'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Daenerys II Targaryen'})
MERGE (end:Dragon {nombre: 'Viserion'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Daenerys II Targaryen'})
MERGE (end:Dragon {nombre: 'Drogon'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Daenerys II Targaryen'})
MERGE (end:Dragon {nombre: 'Rhaegal'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Rhaena II Targaryen'})
MERGE (end:Dragon {nombre: 'Morning'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Aegon I Targaryen'})
MERGE (end:Dragon {nombre: 'Balerion'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Visenya Targaryen'})
MERGE (end:Dragon {nombre: 'Vhagar'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys I Targaryen'})
MERGE (end:Dragon {nombre: 'Meraxes'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Maegor Targaryen'})
MERGE (end:Dragon {nombre: 'Balerion'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Aenys I Targaryen'})
MERGE (end:Dragon {nombre: 'Quicksilver'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Velaryon'})
MERGE (end:Dragon {nombre: 'Meleys'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Rhaena I Targaryen'})
MERGE (end:Dragon {nombre: 'Dreamfyre'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Aegon Targaryen (the Uncrowned)'})
MERGE (end:Dragon {nombre: 'Quicksilver'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys I Targaryen'})
MERGE (end:Dragon {nombre: 'Vermithor'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Alysanne Targaryen'})
MERGE (end:Dragon {nombre: 'Silverwing'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Aerea Targaryen'})
MERGE (end:Dragon {nombre: 'Balerion'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Baelon Targaryen'})
MERGE (end:Dragon {nombre: 'Vhagar'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Alyssa Targaryen'})
MERGE (end:Dragon {nombre: 'Meleys'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Rhaenys II Targaryen'})
MERGE (end:Dragon {nombre: 'Meleys'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Viserys I Targaryen'})
MERGE (end:Dragon {nombre: 'Balerion'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Daemon Targaryen'})
MERGE (end:Dragon {nombre: 'Caraxes'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Rhaenyra Targaryen'})
MERGE (end:Dragon {nombre: 'Syrax'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Laena Velaryon'})
MERGE (end:Dragon {nombre: 'Vhagar'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Laenor Velaryon'})
MERGE (end:Dragon {nombre: 'Seasmoke'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Baela Velaryon'})
MERGE (end:Dragon {nombre: 'Moondancer'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Jacaerys Velaryon'})
MERGE (end:Dragon {nombre: 'Vermax'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Lucerys Velaryon'})
MERGE (end:Dragon {nombre: 'Arrax'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Joffrey Velaryon'})
MERGE (end:Dragon {nombre: 'Tyraxes'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Aegon II Targaryen'})
MERGE (end:Dragon {nombre: 'Sunfyre'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Helaena Targaryen'})
MERGE (end:Dragon {nombre: 'Dreamfyre'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Aemond Targaryen'})
MERGE (end:Dragon {nombre: 'Vhagar'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Daeron Targaryen'})
MERGE (end:Dragon {nombre: 'Tessarion'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Jaehaera Targaryen'})
MERGE (end:Dragon {nombre: 'Morghul'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Jaehaerys Targaryen'})
MERGE (end:Dragon {nombre: 'Shrykos'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Aegon III Targaryen'})
MERGE (end:Dragon {nombre: 'Stormcloud'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Hugh Hammer'})
MERGE (end:Dragon {nombre: 'Vermithor'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Ulf el Blanco'})
MERGE (end:Dragon {nombre: 'Silverwing'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Addam Velaryon'})
MERGE (end:Dragon {nombre: 'Seasmoke'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Nettles'})
MERGE (end:Dragon {nombre: 'Sheepstealer'})
MERGE (start)-[:Jinete]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Alysanne'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Lily'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Willow'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Rosey'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Bellenora Otherys'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Balerion Otherys'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Aegor Rivers'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Mya Rivers'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Gwenys Rivers'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Brynden Rivers'})
MERGE (start)-[:Padre]->(end);

MERGE (start:Personaje {nombre: 'Aegon IV Targaryen'})
MERGE (end:Personaje{nombre: 'Shiera Seastar'})
MERGE (start)-[:Padre]->(end);
