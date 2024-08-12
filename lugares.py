MERGE (n:continente {nombre: 'Poniente',
                descripcion:'Uno de los 4 continentes conocidos, se ubica en el oeste. La mayor parte de este continente pertenece a los Siete Reinos,
una nación soberana que se compone realmente de 9 regiones (el Norte, las Tierras de los Ríos, las Islas del Hierro,
el Valle, las Tierras del Oeste, las Tierras de la Corona, el Dominio, las Tierras de Tormentas y Dorne)  '});
MERGE (n:continente {nombre: 'Essos',
                descripcion:' En el continente de Essos, al este, residen una larga colección de ciudades-estado independientes,
además de vastos territorios de llanuras, ciudades esclavistas y civilizaciones de las que apenas se conoce'});



MERGE (n:region {nombre: 'las Islas del Hierro',religion:'Dios Ahogado',gobierno:'casa Greyjoy',clima:'clima duro y tierras austeras',
                descripcion:'Las islas están formadas por: Pyke, Gran Wyk, Viejo Wyk, Harlaw, Monteorca, Acantilado de Sal, Marea Negra y Luz Solitaria'});

MERGE (start:region {nombre: 'las Islas del Hierro'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:isla {nombre: 'Pyke',
                descripcion:'es el castillo ancestral de la Casa Greyjoy, situado en la isla de su mismo nombre en las Islas del Hierro. '});
MERGE (n:castillo {nombre: 'Pyke',
                descripcion:'es el castillo ancestral de la Casa Greyjoy, situado en la isla de su mismo nombre en las Islas del Hierro. '});


MERGE (start:isla {nombre: 'Pyke'})
MERGE (end:region {nombre: 'las Islas del Hierro'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:castillo {nombre: 'Pyke'})
MERGE (end:isla {nombre: 'Pyke'})
MERGE (start)-[:ubicado_en]->(end);


MERGE (n:region {nombre: 'Tierras de los Ríos',gobierno:'Casa Tully',religion:'Fe de los Siete',clima:'tierras ricas y fertiles',
                descripcion:'  son uno de los Siete Reinos. Delimitan al norte con el reino del Norte, al oeste con las Islas del Hierro, al este con el Valle de Arryn, al sur con las Tierras del Occidente y el Dominio, y al sureste con las Tierras de la Corona, lo que convierte a este reino en una auténtica encrucijada de caminos y
al más expuesto de todos los reinos. Recibe su nombre debido a que el mayor río de todo Poniente, el Tridente, lo atraviesa, junto con todos sus afluentes. '});

MERGE (start:region {nombre: 'Tierras de los Ríos'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'Harrenhal',fundacion:'2 ac',gobierno:'casa Hoare(extinta)-casa Baelish',
                descripcion:'  es el castillo más grande de los Siete Reinos, construido antes de la Guerra de la Conquista.
Fue levantado por orden de Harren el Negro para ser el castillo más grande jamás construido. La destrucción del castillo se debe a que Harren "el Negro" se rehusó a rendirse frente al ejército de Aegon el Conquistador y un par de señores rebeldes de las Tierras de los Ríos'});

MERGE (start:castillo {nombre: 'Harrenhal'})
MERGE (end:region {nombre: 'Tierras de los Ríos'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'Aguasdulces',gobierno:'Casa Tully',religion:'Fe de los Siete',
                descripcion:'es el castillo ancestral de la casa Tully, los señores del Tridente. Los Tullys han gobernado el castillo y sus ricas tierras por al menos miles de años. Se sitúa  en el lado este de las Tierras de los Ríos. El castillo se asienta en la intersección de los ríos Forca Roja y el Piedra Caída.'});

MERGE (start:castillo {nombre: 'Aguasdulces'})
MERGE (end:region {nombre: 'Tierras de los Ríos'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'Los Gemelos',gobierno:'Casa Frey',religion:'Fe de los Siete',
                descripcion:'a veces llamado el Cruce, es el nombre dado a los castillos gemelos y al cruce de río fortificado de la Casa Frey. Se localiza en la zona central de Poniente, sobre el Forca Verde del Tridente.'});

MERGE (start:castillo {nombre: 'Los Gemelos'})
MERGE (end:region {nombre: 'Tierras de los Ríos'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:region {nombre: 'Valle de Arryn',gobierno:'Casa Arryn',religion:'Fe de los Siete',clima:'tierra fertil, area montañosa con inviernos dificiles',
                descripcion:'a veces llamado sólo el Valle, es una de las regiones de los Siete Reinos de Poniente. Fue una nación soberana hasta la Guerra de la Conquista. El Valle es gobernado por la Casa Arryn del Nido de Águilas. El Valle está localizado en la costa este de Poniente, protegida y rodeada de una cadena montañosa impenetrable llamada Montañas de la Luna'});
MERGE (start:region {nombre: 'Valle de Arryn'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'Nido de Águilas',gobierno:'Casa Arryn',religion:'Fe de los Siete',
                descripcion:'El Nido de Águilas es la fortaleza ancestral de la Casa Arryn, una de los más antiguos linajes Ándalos. Localizada en las Montañas de la Luna, al norte del Valle de Arryn, en la ladera del pico Lanza del Gigante. Es considerada inexpugnable e inmune a los ataques. '});
MERGE (start:castillo {nombre: 'Nido de Águilas'})
MERGE (end:region {nombre: 'Valle de Arryn'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:region {nombre: 'Tierras del Oeste',gobierno:'Casa Lannnister',religion:'Fe de los Siete',clima:'campos fertiles y sistemas de montañas y cavernas',
                descripcion:' es una de las regiones de los Siete Reinos de Poniente. Fue una nación soberana hasta la Guerra de la Conquista. Es gobernada por la Casa Lannister de Roca Casterly. Esta tierra siempre ha tenido grandes riquezas y la mayor parte de las edificaciones y dependencias están talladas en la roca, en lo que se considera uno de los mayores logros arquitectónicos de los Siete Reinos. La fortaleza está en una zona rica en minas de oro y nunca ha caído ante un enemigo. Se cree popularmente que la fortaleza parece un león que reposa ante la puesta de sol'});

MERGE (start:region {nombre: 'Tierras del Oeste'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'Roca Casterly',gobierno:'Casa Lannnister',religion:'Fe de los Siete',
                descripcion:'es el asentamiento de la Casa Lannister. La fortaleza se localiza en las Tierras del Oeste de Poniente, ante las costas del Mar del Ocaso. '});

MERGE (start:castillo {nombre: 'Roca Casterly'})
MERGE (end:region {nombre: 'Tierras del Oeste'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:ciudad {nombre: 'Lannisport',
                descripcion:'Es uno de los mayores puertos de los Siete Reinos, justo al Oeste de Roca Casterly, y la ciudad más grande de las Tierras del Oeste. '});

MERGE (start:ciudad {nombre: 'Lannisport'})
MERGE (end:region {nombre: 'Tierras del Oeste'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:region {nombre: 'el Dominio',clima:'el más fertil de poniente',gobierno:'casa Tyrell',religion:'Fe de los Siete',
                descripcion:'es una de las regiones de los Siete Reinos de Poniente. Fue una nación soberana hasta la Guerra de la Conquista. El Dominio es gobernado por la Casa Tyrell del Altojardín. El Dominio es la región más fértil de Poniente y mantiene muchas aldeas y ciudades altamente pobladas. Es la provincia con mayor producción de alimentos del reino.'});

MERGE (start:region {nombre: 'el Dominio'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:ciudad {nombre: 'Antigua',gobierno:'casa Hightower',religion:'Fe de los Siete',
                descripcion:'es la ciudad más antigua de Poniente, la segunda más poblada y uno de sus principales puertos. Es gobernada por la Casa Hightower. Se localiza en el suroeste de Poniente. En ella se encuentra la Ciudadela, lugar de formación de los maestres. '});

MERGE (start:ciudad {nombre: 'Antigua'})
MERGE (end:region {nombre: 'el Dominio'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'el Faro',gobierno:'Casa Hightower',religion:'Fe de los Siete'});

MERGE (start:castillo {nombre: 'el Faro'})
MERGE (end:ciudad {nombre: 'Antigua'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'Altojardín',gobierno:'Casa Tyrell, casa Gardener(extinta)',religion:'Fe de los Siete',
                descripcion:'es el asentamiento de la Casa Tyrell. Antes de la conquista de Poniente por los Targaryen, Altojardín fue el asentamiento de la Casa Gardener. Cuando ese linaje fue destruido en el Campo de Fuego, Harlen Tyrell, el mayordomo de los Gardener rindió la fortaleza a Aegon I. Recibió a cambio el título de Señor del Dominio, con las tierras y honores que eso conllevaba'});

MERGE (start:castillo {nombre: 'Altojardín'})
MERGE (end:region {nombre: 'el Dominio'})
MERGE (start)-[:ubicado_en]->(end);


MERGE (n:region {nombre: 'Tierras de las Tormentas',clima:'propenso a tormentas',gobierno:'casa Baratheon',religion:'Fe de los Siete',
                descripcion:'es una de las regiones de los Siete Reinos de Poniente. Fue una nación soberana hasta la Guerra de la Conquista. Las Tierras de la Tormenta son gobernadas por la Casa Baratheon de Bastión de Tormentas. Es una de las regiones más pequeñas de Poniente, una región de montañas desiertas, costas pedregosas y bosques perennes, incluyendo el Bosquealto, La Selva y el Cabo de la Ira. '});

MERGE (start:region {nombre: 'Tierras de las Tormentas'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'Bastión de Tormentas',gobierno:'casa Baratheon,casa Dundarron (extinta)',religion:'Fe de los Siete',
                   descripcion:'es la sede de la casa Baratheon. Uno de los castillos más fuertes del reino, Bastión de Tormentas fue una vez la sede ancestral de los Reyes de la Casa Tormenta Durrandon que se remonta a muchos miles de años. Se dice que el castillo está protegido por hechizos teñidos en sus propias paredes que impiden que la magia lo afecte o pase por él.'});

MERGE (start:castillo {nombre: 'Bastión de Tormentas'})
MERGE (end:region {nombre: 'Tierras de las Tormentas'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:bahia {nombre: 'Bahía de los Naufragios'});
                   
MERGE (start:bahia {nombre: 'Bahía de los Naufragios'})
MERGE (end:region {nombre: 'Tierras de las Tormentas'})
MERGE (start)-[:ubicado_en]->(end);


MERGE (n:region {nombre: 'Dorne',gobierno:'casa Martell',clima:'desertico',religion:'Fe de los Siete',
                descripcion:'es una gran península que compone la región más sureña de Poniente'});

MERGE (start:region {nombre: 'Dorne'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:ciudad {nombre: 'Lanza de Sol',gobierno:'casa Martell',religion:'Fe de los Siete',
                descripcion:'es la ciudad capital de Dorne en la que se encuentra Palacio Antiguo, el asentamiento de la Casa Martell.'});

MERGE (start:ciudad {nombre: 'Lanza de Sol'})
MERGE (end:region {nombre: 'Dorne'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'Palacio Antiguo',gobierno:'casa Martell',religion:'Fe de los Siete'});

MERGE (start:castillo {nombre: 'Palacio Antiguo'})
MERGE (end:ciudad {nombre: 'Lanza de Sol'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:region {nombre: 'Ciudades Libres',
                descripcion:'son un grupo de nueve ciudades-estado ubicadas en el área occidental de Essos. Comercian e interactúan constantemente con los Siete Reinos de Poniente. Las ciudades que se encuentran en la línea de la costa son Braavos, Pentos, Myr y Volantis, mientras que Lys, Lorath y Tyrosh se asientan en islas frente a la costa. Las ciudades de Norvos y Qohor se localizan en el área interior, al este. '});
MERGE (n:ciudad {nombre: 'Braavos',gobierno:'democratico',religion:'varias/todas',clima:'',fundacion:'1436-500 A.C',
                descripcion:'también conocida como Braavos de las Mil Islas, es la más grande y poderosa de las Ciudades Libres. Se asienta en un archipiélago dentro de una laguna, donde el Mar Angosto se encuentra con el Mar de los Escalofríos. A diferencia de las otras Ciudades Libres, Braavos nunca fue parte del Feudo Franco de Valyria. Fue fundada hacia 500 a.C. por esclavos, que eran llevados en barcos esclavistas hacia una recién fundada colonia valyria en Sothoryos; los esclavos se rebelaron, tomaron control de los barcos y huyeron al "confín más lejano del mundo". '});

MERGE (n:ciudad {nombre: 'Pentos',gobierno:'un principe y un consejo de magisteres',religion:'varias',clima:'',fundacion:'700 B.C',
                descripcion:'Pentos es una gran ciudad portuaria más grande incluso que Astapor, en la Bahía de los Esclavos, y quizá una de las Ciudades Libres más pobladas. La ciudad está delimitada por torres cuadrangulares y edificios de ladrillo.

Es una ciudad rica donde la vida comercial es amplia; comercian con Poniente, con el resto de las Ciudades Libres e incluso con los nómadas Dothraki. Al ser la ciudad de Essos más cercana a Desembarco del Rey, los buques mercantes navegan entre ambas casi a diario '});

MERGE (n:ciudad {nombre: 'Myr',gobierno:'un consejo de magisteres',religion:'varias',clima:'templado',fundacion:'700 A.C',
                descripcion:'es una de las nueve Ciudades Libres ubicadas en Essos. Es una ciudad localizada en la orilla oriental del Mar de la Alegría, a lo largo de la costa occidental de Essos.Su economía fluctúa gracias al comercio. Myr es conocido por sus vinos veraniegos y sus naranjas. Además, es una de las principales Ciudades Libres, colocándose en la tercera más poderosa, luego de Pentos y Braavos. '});

MERGE (n:ciudad {nombre: 'Volantis',gobierno:'democatico, 3 lideres',religion:'varias',clima:'caliente y húmedo',fundacion:'1536 A.C',
                descripcion:'es una de las Ciudades Libres, localizada en la desembocadura del río Rhoyne en Essos. Fue durante algunos años la más poderosa de todas ellas. '});

MERGE (n:ciudad {nombre: 'Lys',gobierno:'un consejo de magisteres',religion:'varias',clima:'soleado y fértil',fundacion:'700 A.C',
                descripcion:'es una de las nueve Ciudades Libres ubicadas en Essos. Se trata de una pequeña ciudad aferrada a las rocas y rodeada por mares tormentosos. Cubre toda una isla frente a la costa sur de Essos '});

MERGE (n:ciudad {nombre: 'Lorath',gobierno:'consejo de principes electos y magisteres',religion:'varias',clima:'',fundacion:'1436 A.C',
                descripcion:' es una de las nueve Ciudades Libres ubicadas en el continente oriental de Essos.  Es una isla en la Bahía de Lorath al suroeste de Braavos',fundacion:'1436 b.c'});

MERGE (n:ciudad {nombre: 'Tyrosh',gobierno:'electo',religion:'varias',
                descripcion:' es una de las nueve Ciudades Libres ubicadas en el continente oriental de Essos. Se encuentra en una isla al norte de los Peldaños de Piedra, al suroeste del continente. El gobernador de Tyrosh es llamado Arconte, el cual es elegido por un consejo de magísteres. Tyrosh es descrita como bulliciosa y caótica. Es más grande que Lanza del Sol. En el puerto se encuentra la Torre Sangrante.'});
MERGE (n:ciudad {nombre: 'Norvos',gobierno:'consejo de magisteres electos por un grupo de sacerdotes',religion:'clérigos barbudos',
                descripcion:' es una de las nueve Ciudades Libres ubicadas en el continente oriental de Essos. Se encuentra en las Colinas de Norvos, tierradentro de Essos. Norvos es una teocracia gobernada por los clérigos barbudos, quienes se rigen por los mandaros que les transmite su dios desde las profundidades de un templo al que sólo los verdaderos creyentes pueden acceder'});

MERGE (n:ciudad {nombre: 'Qohor',gobierno:'',religion:'cabra negra de Qohor',
                descripcion:' es una de las nueve Ciudades Libres ubicadas en Essos y la más oriental de ellas.Es una de las ciudades más rica y la más exótica de ellas, debido a que su posición geográfica la convierte en una puerta al este. Tiene una reputación siniestra, recibiendo el nombre de la Ciudad de los Hechiceros. La ciudad fue fundada por residentes religiosos de Valyria, adoradores de la oscura deidad conocida como la Cabra Negra. El primer asentamiento fue un campamento maderero, que trabajaba la madera procedente del amplio Bosque de Qohor'});

MERGE (n:region {nombre: 'Tierras de la Corona',gobierno:'casa Targaryen, casa Baratheon',religion:'Dioses de Valyria, Fe de los Siete',clima:'templado',
                descripcion:' es una de las nueve regiones de los Siete Reinos de Poniente. Nunca fue un reino independiente sino un área en constante disputa entre los gobernantes de las Tierras de los Ríos, las Tierras de la Tormenta y otros pequeños reinos de la zona. Tras la Guerra de la Conquista el rey Aegon I Targaryen, tras haberla usado como punto de partida para sus campañas, la constituyó como vasalla directa del Trono de Hierro, desvinculándola para siempre de los otros territorios. Su capital es la ciudad de Desembarco del Rey, sede del poder real. '});

MERGE (start:region {nombre: 'Tierras de la Corona'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'Rocadragón',gobierno:'casa Targaryen, casa Baratheon',fundacion:'314 ac',
                   religion:'Dioses de Valyria, Fe de los Siete, Rhllor',
                   descripcion:'la fortaleza ancestral de la Casa Targaryen'});
MERGE (n:isla {nombre: 'Rocadragón',descripcion:'la fortaleza ancestral de la Casa Targaryen'});

MERGE (start:isla {nombre: 'Rocadragón'})
MERGE (end:region {nombre: 'Tierras de la Corona'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:castillo {nombre: 'Rocadragón'})
MERGE (end:isla {nombre: 'Rocadragón'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:isla {nombre: 'Marcaderiva',gobierno:'casa Velaryon',religion:'Fe de los Siete',descripcion:'es una isla al oeste de Rocadragón en la Bahía del Aguas Negras. La fortaleza de la casa Velaryon, los barcos de Driftmark permitieron a los Velaryons controlar el centro del mar angosto antes de la conquista de Aegon. Es una isla baja y fértil, llamada así por la madera a la deriva traida por las mareas. Los asentamientos en la isla han incluido los castillos de Driftmark y High Tide, las ciudades Hull y Spicetown, y astilleros'});

MERGE (start:isla {nombre: 'Marcaderiva'})
MERGE (end:region {nombre: 'Tierras de la Corona'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'Marcaderiva',gobierno:'casa Velaryon',descripcion:'es una isla al oeste de Rocadragón en la Bahía del Aguas Negras. La fortaleza de la casa Velaryon, los barcos de Driftmark permitieron a los Velaryons controlar el centro del mar angosto antes de la conquista de Aegon. Es una isla baja y fértil, llamada así por la madera a la deriva traida por las mareas. Los asentamientos en la isla han incluido los castillos de Driftmark y High Tide, las ciudades Hull y Spicetown, y astilleros'});

MERGE (start:castillo {nombre: 'Marcaderiva'})
MERGE (end:isla {nombre: 'Marcaderiva'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:ciudad {nombre: 'Desembarco del Rey',fundacion:'2 ac',gobierno:'Rey de los Siete Reinos',religion:'Fe de los Siete',
                descripcion:'es la ciudad capital de los Siete Reinos, localizada en la costa este de Poniente, en la bahía del Aguasnegras. Es la sede del Trono de Hierro en la Fortaleza Roja y por tanto el asentamiento del Rey de los Siete Reinos. La ciudad principal está rodeada de una muralla y es custodiada por la Guardia de la Ciudad, también conocidos como los Capas Doradas. Está extremadamente poblada, por lo que es una ciudad sucia y llena de edificaciones de madera y paja. Es el principal puerto de los Siete Reinos, cuyo rival sólo es Antigua. '});

MERGE (start:ciudad {nombre: 'Desembarco del Rey'})
MERGE (end:region {nombre: 'Tierras de la Corona'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:castillo {nombre: 'Fortaleza Roja',gobierno:'casa Targaryen, casa Baratheon',religion:'Fe de los Siete' });

MERGE (start:castillo {nombre: 'Fortaleza Roja'})
MERGE (end:ciudad{nombre: 'Desembarco del Rey'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:region {nombre: 'Ciudades Libres'})
MERGE (end:continente {nombre: 'Essos'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:continente {nombre: 'Sothoryos ',clima:'selvatico',
                descripcion:'Continente ubicado al sur. Se sabe poco de este continente salvo que está habitado por gente de piel oscura y es «selvático, infestado de plagas y principalmente inexplorado>> '});
MERGE (n:continente {nombre: 'Ulthos ',clima:'selvatico',
                descripcion:'Continente ubicado al este. Apenas cartografiado y muy poco explorado '});
MERGE (n:region {nombre: 'el Norte ',gobierno:'casa Stark',clima:'región más fría de Poniente',
                descripcion:'es el más grande de entre todos los Siete Reinos, casi tan grande como los otros seis juntos. Limita al norte con el Muro,
que lo separa de las «tierras del eterno invierno», y al sur con la región de El Cuello que lo mantiene aislado del resto de los reinos sureños. A diferencia de los demás reinos, el Norte se vio aislado de la llegada de los Ándalos,
gracias a que eran detenidos en la región de El Cuello. Debido a esto, los norteños descendían de los Primeros Hombres y conservaron algunas de sus costumbres, como el culto a los Antiguos Dioses.

El Norte fue gobernado desde hacía miles de años por la Casa Stark, cuyo fundador fue Brandon el Constructor, el cual construyó el Muro y la fortaleza de Invernalia. Eso terminó con la llegada de Aegon el Conquistador y sus dragones.
El rey Torrhen Stark quiso combatir a los Targaryen igual que habían hecho con los Ándalos siglos atrás, pero al ver el gran ejército de Aegon y sus dragones, Torrhen decidió rendirse y jurarle lealtad. Aegon permitió a Torrhen continuar
como Señor de Invernalia y le otorgó el título de Guardián del Norte. '});

MERGE (n:region {nombre: 'el Muro',fundacion:'+/- 8000 ac',clima:'nevado todo el año',
                descripcion:' es una inmensa muralla de hielo que se extiende de este a oeste en el norte de Poniente y que separa los Siete Reinos de las tierras salvajes de más allá. Está protegido por la Guardia de la Noche. '});
MERGE (n:castillo {nombre: 'Invernalia',gobierno:'casa Stark',religion:'Antiguos Dioses',fundacion:'+/- 8000 ac',
                   clima:'nevado todo el año',
                descripcion:'es el asentamiento ancestral de la Casa Stark y principal bastión en el Norte. '});

MERGE (start:castillo {nombre: 'Invernalia'})
MERGE (end:region {nombre: 'el Norte'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:region {nombre: 'el Muro'})
MERGE (end:region {nombre: 'el Norte'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:region {nombre: 'el Norte'})
MERGE (end:continente {nombre: 'Poniente'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:ciudad {nombre: 'Valyria',religion:'Dioses de Valyria',fundacion:'+/- 5000 ac',
                descripcion:'también llamada Antigua Valyria, es una ciudad en ruinas en Essos y antigua capital del Feudo Franco de Valyria. Fue destruida junto a todo el imperio por un cataclismo conocido como la Maldición de Valyria '});
MERGE (n:region {nombre: 'Feudo Franco de Valyria',
                descripcion:'fue un gran imperio que abarcó gran parte del continente de Essos y que se derrumbó aproximadamente unos cien años antes del Desembarco de Aegon, cuando fue arrasado por un cataclismo conocido como la Maldición de Valyria.
En su apogeo, llegaba hasta las actuales Ciudades Libres, a Rhoyne, a la Bahía de los Esclavos y a la Isla de Rocadragón, en las costas de Poniente. El Feudo Franco de Valyria era una civilización tecnológicamente avanzada y con una milicia dominante cuyo poder cultural es aún recordado. Su capital era la ciudad de Valyria.  '});

MERGE (start:ciudad {nombre: 'Valyria'})
MERGE (end:region {nombre: 'Feudo Franco de Valyria'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:ciudad {nombre: 'Braavos'})
MERGE (end:region {nombre: 'Ciudades Libres'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:ciudad {nombre: 'Pentos'})
MERGE (end:region {nombre: 'Ciudades Libres'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:ciudad {nombre: 'Myr'})
MERGE (end:region {nombre: 'Ciudades Libres'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:ciudad {nombre: 'Volantis'})
MERGE (end:region {nombre: 'Ciudades Libres'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:ciudad {nombre: 'Lys'})
MERGE (end:region {nombre: 'Ciudades Libres'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:ciudad{nombre: 'Lorath'})
MERGE (end:region {nombre: 'Ciudades Libres'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:ciudad {nombre: 'Tyrosh'})
MERGE (end:region {nombre: 'Ciudades Libres'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:ciudad {nombre: 'Norvos'})
MERGE (end:region {nombre: 'Ciudades Libres'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (start:ciudad {nombre: 'Qohor'})
MERGE (end:region {nombre: 'Ciudades Libres'})
MERGE (start)-[:ubicado_en]->(end);

MERGE (n:mar {nombre: 'Mar Angosto',descripcion:'es el mar que divide a Poniente de Essos' });

MERGE (n:bahia {nombre: 'Bahía del Aguasnegras' });

MERGE (start:bahia {nombre: 'Bahía del Aguasnegras'})
MERGE (end:region {nombre: 'Tierras de la Corona'})
MERGE (start)-[:ubicado_en]->(end);
