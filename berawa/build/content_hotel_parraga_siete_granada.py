# Contenido de la demo Hotel Párraga Siete (Granada) (es/en/fr/de). Hechos de hotelparragasiete.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin precios de habitacion ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächlichen Zimmer.'}
H={'es':['Individuales y dobles','Ejecutivas y apartamento'],'en':['Singles and doubles','Executive rooms and apartment'],'fr':['Individuelles et doubles','Chambres exécutives et appartement'],'de':['Einzel- und Doppelzimmer','Executive-Zimmer und Apartment']}
RD={
'es':['Individual estándar y deluxe, doble estándar de 18 m² y doble deluxe de 18 m² con 2 camas individuales o 1 cama doble. Aire acondicionado, calefacción, TV de pantalla plana, escritorio y WiFi gratis.','Doble y triple ejecutivas de 28 m² con balcón y sofá (la triple, con sofá cama). Y un apartamento de 100 m² junto al hotel, con salón cocina, una habitación, dos baños y parking incluido.'],
'en':['Standard and deluxe singles, an 18 m² standard double and an 18 m² deluxe double with 2 single beds or 1 double bed. Air conditioning, heating, flat-screen TV, desk and free WiFi.','28 m² executive double and triple rooms with balcony and sofa (a sofa bed in the triple). Plus a 100 m² apartment next to the hotel, with living room and kitchen, one bedroom, two bathrooms and parking included.'],
'fr':['Individuelles standard et deluxe, double standard de 18 m² et double deluxe de 18 m² avec 2 lits simples ou 1 lit double. Climatisation, chauffage, TV écran plat, bureau et WiFi gratuit.','Double et triple exécutives de 28 m² avec balcon et canapé (canapé-lit dans la triple). Et un appartement de 100 m² près de l\'hôtel, avec salon-cuisine, une chambre, deux salles de bains et parking inclus.'],
'de':['Einzelzimmer Standard und Deluxe, Doppelzimmer Standard mit 18 m² und Doppelzimmer Deluxe mit 18 m², mit 2 Einzelbetten oder 1 Doppelbett. Klimaanlage, Heizung, Flachbildfernseher, Schreibtisch und kostenloses WLAN.','Executive-Doppel- und Dreibettzimmer mit 28 m², Balkon und Sofa (im Dreibettzimmer ein Schlafsofa). Dazu ein 100-m²-Apartment beim Hotel mit Wohnküche, einem Schlafzimmer, zwei Bädern und inklusive Parkplatz.']}
ART={
'hero':('arches',9401,['#f2e8da','#f7f1e7','#7a2e2a','#4e1c1a','#2b0f0e']),
'intro':('columns',9402,['#efe5d4','#e2b27a','#7a2e2a','#4e1c1a','#2b0f0e']),
'r1':('skyline',9411,['#4e1c1a','#e6a565','#f4d5a2','#3d5a3e','#2f4a31','#1d3020']),
'r2':('hills',9412,['#ece9de','#f2e6cc','#e5b46e','#a3b08a','#76896a','#4f6249']),
'g1':('arches',9421,['#7a2e2a','#ecbf86','#f6dfb6','#9a4a3a','#7a2e2a','#4e1c1a']),
'g2':('columns',9422,['#edeae2','#f7f4ee','#3d5a3e','#4e1c1a','#2b0f0e']),
'g3':('waves',9423,['#ecdfca','#dcab76','#9e4224','#4e1c1a','#2b0f0e']),
'g4':('skyline',9424,['#4e1c1a','#e0a064','#f2cf9c','#3b5a3c','#2d4a2f','#1b301d'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Párraga Siete · Hotel con encanto en el casco antiguo de Granada',see_rooms='Ver las habitaciones',hero_k='Granada · Casco antiguo',hero_t='Pequeño y refinado hotel con encanto en el corazón de Granada',hero_s='Una casa clásica del siglo XIX rehabilitada, a 5 minutos a pie de la catedral.',
 intro_t='Tu casa en el centro de Granada',intro_p1='20 habitaciones elegantes y amplias, de decoración contemporánea, alrededor de un patio interior que deja pasar la luz natural.',
 intro_p2='El hotel alberga el restaurante Blu Vitola, con bodega propia, cocina local y cócteles. Cada día, desde las 07:00, cesta de desayuno en la habitación.',
 stats=['Casa del siglo XIX','20 habitaciones','WiFi gratis','Restaurante Blu Vitola'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='De la individual estándar a la triple ejecutiva, más un apartamento con parking.',
 svcs=['Patio interior','Rincón de té y café','Cesta de desayuno en la habitación','Adaptado a movilidad reducida','Guardaequipaje','Asesoramiento para el tour de la Alhambra'],
 around_s='Granada: la Alhambra, el Generalife, el barrio del Albaicín, el Sacromonte y el Paseo de los Tristes.',
 loc_p='Calle Párraga, 7 · 18002 Granada, en el casco antiguo, a 5 minutos a pie de la catedral.',
 chips=['¿Qué habitaciones tenéis?','¿Tenéis apartamento?','¿Hay desayuno?','¿Dónde está el hotel?']),
'en':dict(title='Hotel Párraga Siete · Charming hotel in the old town of Granada',see_rooms='See the rooms',hero_k='Granada · Old town',hero_t='A small, refined hotel with charm in the heart of Granada',hero_s='A restored classic 19th-century house, a 5-minute walk from the cathedral.',
 intro_t='Your home in central Granada',intro_p1='20 elegant, spacious rooms with contemporary décor, around an inner patio that lets in natural light.',
 intro_p2='The hotel houses the Blu Vitola restaurant, with its own wine cellar, local cuisine and cocktails. Every day from 07:00, a breakfast basket in your room.',
 stats=['19th-century house','20 rooms','Free WiFi','Blu Vitola restaurant'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='From the standard single to the executive triple, plus an apartment with parking.',
 svcs=['Inner patio','Tea and coffee corner','Breakfast basket in your room','Adapted for reduced mobility','Luggage storage','Help booking the Alhambra tour'],
 around_s='Granada: the Alhambra, the Generalife, the Albaicín quarter, Sacromonte and the Paseo de los Tristes.',
 loc_p='Calle Párraga, 7 · 18002 Granada, in the old town, a 5-minute walk from the cathedral.',
 chips=['Which rooms do you have?','Do you have an apartment?','Is there breakfast?','Where is the hotel?']),
'fr':dict(title='Hotel Párraga Siete · Hôtel de charme dans la vieille ville de Grenade',see_rooms='Voir les chambres',hero_k='Grenade · Vieille ville',hero_t='Un petit hôtel de charme raffiné au cœur de Grenade',hero_s='Une maison classique du XIXe siècle restaurée, à 5 minutes à pied de la cathédrale.',
 intro_t='Votre maison au centre de Grenade',intro_p1='20 chambres élégantes et spacieuses, au décor contemporain, autour d\'un patio intérieur qui laisse entrer la lumière naturelle.',
 intro_p2='L\'hôtel abrite le restaurant Blu Vitola, avec sa propre cave, une cuisine locale et des cocktails. Chaque jour dès 07:00, panier petit-déjeuner en chambre.',
 stats=['Maison du XIXe siècle','20 chambres','WiFi gratuit','Restaurant Blu Vitola'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='De l\'individuelle standard à la triple exécutive, plus un appartement avec parking.',
 svcs=['Patio intérieur','Coin thé et café','Panier petit-déjeuner en chambre','Adapté aux personnes à mobilité réduite','Bagagerie','Conseils pour réserver la visite de l\'Alhambra'],
 around_s='Grenade : l\'Alhambra, le Generalife, le quartier de l\'Albaicín, le Sacromonte et le Paseo de los Tristes.',
 loc_p='Calle Párraga, 7 · 18002 Grenade, dans la vieille ville, à 5 minutes à pied de la cathédrale.',
 chips=['Quelles chambres avez-vous ?','Avez-vous un appartement ?','Y a-t-il un petit-déjeuner ?',"Où se trouve l'hôtel ?"]),
'de':dict(title='Hotel Párraga Siete · Charmantes Hotel in der Altstadt von Granada',see_rooms='Zimmer ansehen',hero_k='Granada · Altstadt',hero_t='Ein kleines, feines Hotel mit Charme im Herzen von Granada',hero_s='Ein restauriertes klassisches Haus aus dem 19. Jahrhundert, 5 Gehminuten von der Kathedrale.',
 intro_t='Ihr Zuhause im Zentrum von Granada',intro_p1='20 elegante, geräumige Zimmer mit zeitgemäßer Einrichtung rund um einen Innenhof, der Tageslicht hereinlässt.',
 intro_p2='Im Hotel befindet sich das Restaurant Blu Vitola mit eigenem Weinkeller, lokaler Küche und Cocktails. Täglich ab 07:00 Uhr ein Frühstückskorb auf dem Zimmer.',
 stats=['Haus aus dem 19. Jh.','20 Zimmer','Kostenloses WLAN','Restaurant Blu Vitola'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Vom Standard-Einzelzimmer bis zum Executive-Dreibettzimmer, dazu ein Apartment mit Parkplatz.',
 svcs=['Innenhof','Tee- und Kaffee-Ecke','Frühstückskorb auf dem Zimmer','Barrierefrei','Gepäckaufbewahrung','Hilfe bei der Buchung der Alhambra-Tour'],
 around_s='Granada: Alhambra, Generalife, das Albaicín-Viertel, Sacromonte und der Paseo de los Tristes.',
 loc_p='Calle Párraga, 7 · 18002 Granada, in der Altstadt, 5 Gehminuten von der Kathedrale.',
 chips=['Welche Zimmer gibt es?','Haben Sie ein Apartment?','Gibt es Frühstück?','Wo liegt das Hotel?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB={'es':'https://www.hotelparragasiete.com/reservas/','en':'https://www.hotelparragasiete.com/en/reservas/','fr':'https://www.hotelparragasiete.com/fr/reservas/','de':'https://www.hotelparragasiete.com/en/reservas/'}
BOOK=dict(mode='engine',url=RB)
D=dict(name='Hotel Párraga Siete',ac='#4e1c1a',ac2='#3d5a3e',ac2_a11y='#2f4a31',book=BOOK,around=['Alhambra','Albaicín'],foot=FOOT,
 address='Calle Párraga, 7 · 18002 Granada',phones=['+34 958 264 227'],emails=['info@hotelparragasiete.com'],maps='Hotel Párraga Siete, Calle Párraga 7, Granada',t=T)
META=dict(repo='demo-hotel-parraga-siete-granada',name='Hotel Párraga Siete',legal_name='AUTOMÁTICOS PUERTA REAL, S.L.',registry_ids=['CIF B18457853'],
 url='https://www.hotelparragasiete.com/',domain='hotelparragasiete.com',municipality='Granada',province='Granada',sector='hotel con encanto de 20 habitaciones en una casa del siglo XIX en el casco antiguo de Granada',
 read_at='2026-10-30T07:09:09+01:00',created_at='2026-10-30T07:08:30+01:00',built_at='2026-10-30T07:20:00+01:00',audit_date='2026-10-30T06:50:00+01:00',
 rating=dict(value=4.4,coincide=['telefono','web'],date='2026-10-29T11:02:09+01:00',url='https://www.google.com/maps/place/Hotel+P%C3%A1rraga+Siete/@37.1734602,-3.6007947,17z/data=!4m9!3m8!1s0xd71fcbe0ed46ee5:0x148ff125d250ddd9!5m2!4m1!1i2!8m2!3d37.1734602!4d-3.6007947!16s%2Fg%2F11xqspd3_'),
 book=dict(mode='engine',url=RB['es'],note='página de reservas real de su web (/reservas/, /en/reservas/, /fr/reservas/), HTTP 200 comprobado el 30/10/2026; su web no tiene alemán, así que DE abre la versión inglesa.'),first_of_type=None)
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Tenéis apartamento?','K02'),('¿Hay parking?','K03'),('¿Hay desayuno?','K04'),('¿Qué tal es el restaurante?','K05'),('¿Hay wifi?','K06'),('¿Puedo hacer el check-in online?','K07'),('¿Dónde está el hotel?','K08'),('¿Me ayudáis con la Alhambra?','K09'),('¿Cómo reservo?','K10'),('¿Podéis confirmarme disponibilidad para mañana?','K10'),('¿Cuánto cuesta una noche?',None),('¿Admitís mascotas?',None)],
'en':[('Which rooms do you have?','K01'),('Do you have an apartment?','K02'),('Is there parking?','K03'),('Is there breakfast?','K04'),('What is the restaurant like?','K05'),('Is there wifi?','K06'),('Can I do online check-in?','K07'),('Where is the hotel?','K08'),('Can you help me with the Alhambra?','K09'),('How do I book?','K10'),('Can you confirm availability for tomorrow?','K10'),('How much is a night?',None),('Do you allow pets?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Avez-vous un appartement ?','K02'),('Y a-t-il un parking ?','K03'),('Y a-t-il un petit-déjeuner ?','K04'),('Comment est le restaurant ?','K05'),('Y a-t-il le wifi ?','K06'),('Puis-je faire le check-in en ligne ?','K07'),("Où se trouve l'hôtel ?",'K08'),("Pouvez-vous m'aider pour l'Alhambra ?",'K09'),('Comment réserver ?','K10'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K10'),('Combien coûte une nuit ?',None),('Acceptez-vous les animaux ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Haben Sie ein Apartment?','K02'),('Gibt es einen Parkplatz?','K03'),('Gibt es Frühstück?','K04'),('Wie ist das Restaurant?','K05'),('Gibt es WLAN?','K06'),('Kann ich online einchecken?','K07'),('Wo liegt das Hotel?','K08'),('Können Sie mir bei der Alhambra helfen?','K09'),('Wie kann ich buchen?','K10'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K10'),('Was kostet eine Übernachtung?',None),('Sind Haustiere erlaubt?',None)]}
