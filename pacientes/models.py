from django.db import models
import datetime
from labs.exportable import CSVExportable, PDFExportable

# Modelo central
class Paciente(models.Model, CSVExportable, PDFExportable):
    # --- informacion demografica ---
    sexos = (
        (u'F', u'Femenino'),
        (u'M', u'Masculino'),
    )
    sexo = models.CharField(max_length=1, default='F', choices=sexos)
    nacimiento = models.DateField(verbose_name='fecha de nacimiento')
    razas = (
        (u"latino", u"latino"),
        (u"mapuche", u"mapuche"),
        (u"otras etnias", u"otras etnias"),
        (u"anglosaj\u00F3n", u"anglosaj\u00F3n"),
        (u"espa\u00F1ol", u"espa\u00F1ol"),
        (u"otro (indique cual abajo)", u"otro (indique cual abajo)"),
    )
    raza = models.CharField(max_length=30, verbose_name="raza / etnia", choices=razas, default=u"latino")
    raza_otro = models.CharField(max_length=40, verbose_name="otra raza", help_text=u"Indique aqu\u00ED la raza del paciente si seleccion\u00F3 \"otro\" en el campo anterior", blank=True)
    # --- informacion genetica ---
    sino = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    test_genetico = models.CharField(verbose_name=u"test gen\u00E9tico", help_text=u"Indique si el paciente fue sometido al test gen\u00E9tico para HD", max_length=1, choices=sino, default='N')
    tripletes = models.IntegerField(verbose_name=u'n\u00FAmero de tripletes')
    # --- consentimiento ---
    fecha_consentimiento = models.DateField(verbose_name="fecha de consentimiento", blank=True, null=True)
    # --- historial de hd ---
    fecha_diagnostico = models.DateField(verbose_name=u"fecha del diagn\u00F3stico", blank=True, null=True)
    #parientes, fk a modelo Familiar
    fecha_sintomas = models.DateField(verbose_name=u"aparici\u00F3n de s\u00EDntomas", help_text=u"Indique la fecha de aparici\u00F3n de s\u00EDntomas motores,<br />o deje en blanco si se desconoce", blank=True, null=True)
    fecha_tratamiento = models.DateField(verbose_name=u"tratamiento inicial", help_text=u"Indique el comienzo del tratamiento inicial", blank=True, null=True)
    medicacion = models.CharField(verbose_name=u"medicaci\u00F3n", help_text=u"Indique si el paciente ha estado en medicaci\u00F3n estable por las \u00FAltimas 4 semanas", max_length=1, choices=sino, default='N')
    medicacion_glosa = models.TextField(verbose_name=u"detalle de medicaci\u00F3n", help_text=u"Indique los medicamentos, si los hubo", max_length=1000, blank=True)
    # --- historial neurologico ---
    enfermedades_pasadas = models.CharField(verbose_name=u"enfermedades pasadas", help_text=u"Indique si el paciente ha tenido enfermedades en el pasado, y cuales", max_length=1, choices=sino, default='N')
    enfermedades_pasadas_glosa = models.TextField(verbose_name=u"enfermedades", max_length=1000, blank=True)
    # --- historial de cirugia ---
    cirugias = models.CharField(verbose_name=u"procedimientos quir\u00FArgicos", help_text=u"Indique si el paciente a tenido procedimientos quir\u00FArgicos relevantes, y cuales", max_length=1, choices=sino, default='N')
    cirugias_glosa = models.TextField(verbose_name=u"cirug\u00EDas", max_length=1000, blank=True)

    def __unicode__(self):
        return "paciente ID {0}".format(self.id)

    def numero_familiares(self):
        return self.familiar_set.count()
    numero_familiares.short_description = u"n\u00B0 de familiares"

    def edad(self):
        delta = datetime.date.today() - self.nacimiento
        if delta.days > 365:
            agnos = int(delta.days/365.2425)
            meses = int(delta.days%365.2425)/30
            return u"{0} a\u00F1os {1} meses".format(agnos, meses)
        else:
            meses = delta.days/30
            dias = delta.days%30
            return u"{0} meses {1} d\u00EDas".format(meses, dias)

    def evaluaciones_funcionales(self):
        return self.evaluacionfuncional_set.count()
    evaluaciones_funcionales.short_description = u"n\u00B0 eval. funcionales"

    def evaluaciones_motoras(self):
        return self.evaluacionmotora_set.count()
    evaluaciones_motoras.short_description = u"n\u00B0 eval. motoras"

    def neuroimagenes(self):
        return self.neuroimagen_set.count()
    neuroimagenes.short_description = u"neuroim\u00E1genes"

    def fecha_ultima_revision(self):
        efunc = self.evaluacionfuncional_set.order_by('-fecha')
        emotor = self.evaluacionmotora_set.order_by('-fecha')
        esignos = self.examensignosvitales_set.order_by('-fecha')
        efisico = self.examenfisico_set.order_by('-fecha')
        eneuro = self.examenneurologico_set.order_by('-fecha')
        examenes = filter(lambda x: x.count() > 0, [efunc, emotor, esignos, efisico, eneuro])
        fechas = map(lambda x: x[0].fecha, examenes)
        fecha = None
        if len(fechas) > 0:
            fecha = max(fechas)
        if fecha is None:
            return "<no hay>"
        return fecha.strftime('%d/%m/%Y')
    fecha_ultima_revision.short_description = u"\u00FAltima revisi\u00F3n"

    # Exportacion
    def get_csv_pairs(self):
        return [
            ("id",                                  self.id),
            (u"fecha de nac.",                      self.nacimiento.isoformat()),
            (u"sexo",                               self.sexo),
            (u"raza / etnia",                       self.raza if self.raza != self.razas[-1][0] else self.raza_otro),
            (u"\u00BFtest gen\u00E9tico?",          self.test_genetico),
            (u"num. tripletes",                     self.tripletes),
            (u"fecha de consentimiento",            "" if self.fecha_consentimiento is None else self.fecha_consentimiento.isoformat()),
            (u"fecha del diagn\u00F3stico",         "" if self.fecha_diagnostico is None else self.fecha_diagnostico.isoformat()),
            (u"num. familiares enfermos",           self.numero_familiares()),
            (u"fecha aparici\u00F3n s\u00EDntomas", "" if self.fecha_sintomas is None else self.fecha_sintomas.isoformat()),
            (u"inicio de tratamiento",              "" if self.fecha_tratamiento is None else self.fecha_tratamiento.isoformat()),
            (u"medicaci\u00F3n",                    self.medicacion_glosa if self.medicacion == 'S' else ""),
            (u"enfermedades pasadas",               self.enfermedades_pasadas_glosa if self.enfermedades_pasadas == 'S' else ""),
            (u"cirug\u00EDas",                      self.cirugias_glosa if self.cirugias == 'S' else ""),
            (u"num. evaluaciones funcionales",      self.evaluaciones_funcionales()),
            (u"num. evaluaciones motoras",          self.evaluaciones_motoras()),
            (u"num. neuroim\u00E1genes",            self.neuroimagenes()),
            (u"\u00FAltima revisi\u00F3n",          self.fecha_ultima_revision())
        ]

    def get_pdf_pairs(self):
        return [
            (u"Paciente",                  self),
            (u"Fecha de nacimiento",       self.nacimiento),
            (u"Sexo",                      dict(self.sexos)[self.sexo]),
            (u"N\u00B0 de familiares",     self.numero_familiares()),
            (u"N\u00B0 eval. motoras",     self.evaluaciones_motoras()),
            (u"N\u00B0 eval. funcionales", self.evaluaciones_funcionales()),
            (u"\u00DAltima revisi\u00F3n", self.fecha_ultima_revision())
        ]

# Familiares tambien enfermos
class Familiar(models.Model):
    paciente = models.ForeignKey(Paciente)
    parentesco = models.CharField(max_length=50)
    def __unicode__(self):
        return u"{0} de paciente ID {1}".format(self.parentesco, self.paciente.id)
    
    class Meta:
        verbose_name_plural = "familiares"

# Texto con la explicacion de las escalas de evualuacion motora
motor_scales = [
    (u"seguimiento ocular", [
        u"0 = completo (normal)",
        u"1 = movimiento sac\u00E1dico",
        u"2 = seguimiento interrumpido (rango completo)",
        u"3 = rango incompleto",
        u"4 = no logra seguimiento"
    ]),
    (u"inicio s\u00E1cadas", [
        u"0 = normal",
        u"1 = aumento de latencia",
        u"2 = pesta\u00F1eo o movimientos cef\u00E1licos controlables al iniciar",
        u"3 = movimientos cef\u00E1licos no suprimibles",
        u"4 = no puede iniciar s\u00E1cadas"
    ]),
    (u"velocidad s\u00E1cadas", [
        u"0 = normal",
        u"1 = enlentecimiento leve",
        u"2 = enlentecimiento moderado",
        u"3 = muy lento, rango completo",
        u"4 = rango incompleto"
    ]),
    (u"disartria", [
        u"0 = normal",
        u"1 = poco claro. No requiere repetir",
        u"2 = debe repetir para ser comprendido",
        u"3 = casi incomprensible",
        u"4 = mutismo"
    ]),
    (u"protrusi\u00F3n lingual", [
        u"0 = puede mantener lengua protruida por 10 segundos",
        u"1 = no puede mantener completamente protruida por 10 segundos",
        u"2 = no puede mantener completamente protruida por 5 segundos",
        u"3 = no puede protruir completamente",
        u"4 = no puede protruir m\u00E1s all\u00E1 de los labios"
    ]),
    (u"m\u00E1ximo de diston\u00EDa", [
        u"0 = ausente",
        u"1 = leve/intermitente",
        u"2 = moderada/com\u00FAn o moderada/intermitente",
        u"3 = moderada/com\u00FAn",
        u"4 = marcada/prolongada"
    ]),
    (u"m\u00E1ximo de corea", [
        u"0 = ausente",
        u"1 = leve/intermitente",
        u"2 = moderada/com\u00FAn o moderada/intermitente",
        u"3 = moderada/com\u00FAn",
        u"4 = marcada/prolongada"
    ]),
    (u"prueba de tensi\u00F3n de retropulsi\u00F3n", [
        u"0 = normal",
        u"1 = se recupera espont\u00E1neamente",
        u"2 = se caer\u00EDa si no se atrapa",
        u"3 = tiende a caerse espont\u00E1neamente",
        u"4 = no puede mantenerse de pie"
    ]),
    (u"digitaci\u00F3n", [
        u"0 = normal (>= 15/5 seg)",
        u"1 = disminuci\u00F3n leve de velocidad o reducci\u00F3n en amplitud (11-14/5 seg)",
        u"2 = moderadamente discapacitado. Fatiga definitiva y temprana. Puede tener espasmos ocacionales en movimiento (7-10/5 seg)",
        u"3 = severamente discapacitado. Duda frecuente al iniciar movimientos o espasmos en movimientos en curso (3-6/5 seg)",
        u"4 = a penas puede realizar la tarea (0-2/5 seg)"
    ]),
    (u"pronaci\u00F3n/supinaci\u00F3n de manos", [
        u"0 = normal",
        u"1 = disminuci\u00F3n leve de velocidad y/o irregular",
        u"2 = disminuci\u00F3n moderada de velocidad e irregular",
        u"3 = disminuci\u00F3n severa de velocidad e irregular",
        u"4 = no puede realizar"
    ]),
    (u"luria", [
        u"0 = >=4 en 10 segundos, sin se\u00F1al",
        u"1 = < 4 en 10 segundos, sin se\u00F1al",
        u"2 = >=4 en 10 segundos, con se\u00F1al",
        u"3 = < 4 en 10 segundos, con se\u00F1ales",
        u"4 = no puede realizar"
    ]),
    (u"rigidez de brazos", [
        u"0 = ausente",
        u"1 = leve o presente s\u00F3lo con activaci\u00F3n",
        u"2 = leve a moderada",
        u"3 = severa, todo el rango de movimiento",
        u"4 = severa con rango limitado"
    ]),
    (u"lentitud de movimiento - cuerpo", [
        u"0 = normal",
        u"1 = m\u00EDnimamente lento (? normal)",
        u"2 = leve pero claramente lento",
        u"3 = moderadamente lento, con dudas",
        u"4 = marcadamente lento, largas demoras en la iniciaci\u00F3n"
    ]),
    (u"paso", [
        u"0 = paso normal, base estrecha",
        u"1 = base ancha y/o lento",
        u"2 = base ancha y camina con dificultad",
        u"3 = s\u00F3lo camina con ayuda",
        u"4 = no puede intentar"
    ]),
    (u"caminar en t\u00E1ndem", [
        u"0 = normal en 10 pasos",
        u"1 = de 1 a 3 desviaciones de una l\u00EDnea recta",
        u"2 = > 3 desviaciones",
        u"3 = no puede completar",
        u"4 = no puede intentar"
    ])
]

mnames = map(lambda x: x[0], motor_scales)
mscales = map(lambda x: u"<span style=\"color: #333333;\">{0}</span>".format("<br />".join(x[1])), motor_scales)

# Evaluaciones motoras periodicas
class EvaluacionMotora(models.Model, CSVExportable, PDFExportable):
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateField()
    # Puntajes
    choices4 = tuple(map(lambda x: (x,str(x)), range(5)))
    ocular_pursuit = models.IntegerField(verbose_name=mnames[0], help_text=mscales[0], choices=choices4, blank=True, null=True)
    saccade_initiation = models.IntegerField(verbose_name=mnames[1], help_text=mscales[1], choices=choices4, blank=True, null=True)
    saccade_velocity = models.IntegerField(verbose_name=mnames[2], help_text=mscales[2], choices=choices4, blank=True, null=True)
    dysarthria = models.IntegerField(verbose_name=mnames[3], help_text=mscales[3], choices=choices4, blank=True, null=True)
    tongue_protrusion = models.IntegerField(verbose_name=mnames[4], help_text=mscales[4], choices=choices4, blank=True, null=True)
    maximal_dystonia = models.IntegerField(verbose_name=mnames[5], help_text=mscales[5], choices=choices4, blank=True, null=True)
    maximal_chorea = models.IntegerField(verbose_name=mnames[6], help_text=mscales[6], choices=choices4, blank=True, null=True)
    retropulsion_pull_test = models.IntegerField(verbose_name=mnames[7], help_text=mscales[7], choices=choices4, blank=True, null=True)
    finger_taps = models.IntegerField(verbose_name=mnames[8], help_text=mscales[8], choices=choices4, blank=True, null=True)
    pronate_supinate_hands = models.IntegerField(verbose_name=mnames[9], help_text=mscales[9], choices=choices4, blank=True, null=True)
    luria = models.IntegerField(verbose_name=mnames[10], help_text=mscales[10], choices=choices4, blank=True, null=True)
    rigidity_arms = models.IntegerField(verbose_name=mnames[11], help_text=mscales[11], choices=choices4, blank=True, null=True)
    bradykinesia_body = models.IntegerField(verbose_name=mnames[12], help_text=mscales[12], choices=choices4, blank=True, null=True)
    gait = models.IntegerField(verbose_name=mnames[13], help_text=mscales[13], choices=choices4, blank=True, null=True)
    tandem_walking = models.IntegerField(verbose_name=mnames[14], help_text=mscales[14], choices=choices4, blank=True, null=True)

    def respuestas(self):
        return [
            self.ocular_pursuit,
            self.saccade_initiation,
            self.saccade_velocity,
            self.dysarthria,
            self.tongue_protrusion,
            self.maximal_dystonia,
            self.maximal_chorea,
            self.retropulsion_pull_test,
            self.finger_taps,
            self.pronate_supinate_hands,
            self.luria,
            self.rigidity_arms,
            self.bradykinesia_body,
            self.gait,
            self.tandem_walking
        ]

    def efectuadas(self):
        return len(filter(lambda x: x is not None, self.respuestas()))
    efectuadas.short_description = u"n\u00B0 de preguntas"

    def total_puntaje(self):
        def add_none(a, b):
            if b is None:
                return a
            return a + b
        return reduce(add_none, self.respuestas(), 0)
    total_puntaje.short_description = u"puntaje total"

    def __unicode__(self):
        return u"eval. motora de {0}".format(self.paciente)

    # Exportacion
    def get_csv_pairs(self):
        format_none = lambda x: "<en blanco>" if x is None else x
        return [
            ("id paciente",             self.paciente.pk),
            ("fecha",                   self.fecha.isoformat()),
            ("evaluaciones efectuadas", self.efectuadas()),
            ("puntaje total",           self.total_puntaje())
        ] + map(lambda x,y: (x,y), mnames, map(format_none, self.respuestas()))

    def get_pdf_pairs(self):
        return [
            (u"Evaluaci\u00F3n motora", self),
            (u"Fecha",                  self.fecha),
            (u"N\u00B0 de preguntas",   self.efectuadas()),
            (u"Puntaje total",          self.total_puntaje())
        ]
 
    class Meta:
        verbose_name = u'evaluaci\u00F3n motora'
        verbose_name_plural = u'evaluaciones motoras'

# Tal vez crear modelo aparte para las preguntas?
# problema: admin de django tendria que ser personalizado
questions = [
    u"\u00BFPudo (pod\u00EDa) el paciente participar en un empleo remunerado en su trabajo de costumbre?",
    u"\u00BFPudo el paciente participar en alg\u00FAn tipo de empleo remunerado?",
    u"\u00BFPudo el paciente participar en alg\u00FAn tipo de empleo voluntario o no remunerado?",
    u"\u00BFPudo el paciente administrar sus finanzas (mensualmente) sin ayuda alguna?",
    u"\u00BFPudo el paciente comprar comestibles sin ayuda?",
    u"\u00BFPudo el paciente manipular dinero como comprador en una transacci\u00F3n simple?",
    u"\u00BFPudo el paciente cuidar ni\u00F1os sin ayuda?",
    u"\u00BFPudo el paciente manejar un autom\u00F3bil de forma segura e independiente?",
    u"\u00BFPudo el paciente realizar sus tareas del hogar sin ayuda?",
    u"\u00BFPudo el paciente lavar su ropa sin ayuda?",
    u"\u00BFPudo el paciente preparar sus comidas sin ayuda?",
    u"\u00BFPudo el paciente usar el tel\u00E9fono sin ayuda?",
    u"\u00BFPudo el paciente tomar sus medicamentos sin ayuda?",
    u"\u00BFPudo el paciente alimentarse sin ayuda?",
    u"\u00BFPudo el paciente vestirse sin ayuda?",
    u"\u00BFPudo el paciente ba\u00F1arse sin ayuda?",
    u"\u00BFPudo el paciente usar el transporte p\u00FAblico para movilizarse sin ayuda?",
    u"\u00BFPudo el paciente caminar en su vecindario sin ayuda?",
    u"\u00BFPudo el paciente caminar sin caer?",
    u"\u00BFPudo el paciente caminar sin ayuda?",
    u"\u00BFPudo el paciente peinar su cabello sin ayuda?",
    u"\u00BFPudo el paciente cambiarse de sillas sin ayuda?",
    u"\u00BFPudo el paciente acostarse y levantarse de la cama sin ayuda?",
    u"\u00BFPudo el paciente usar el inodoro/c\u00F3moda sin ayuda?",
    u"\u00BFFue posible cuidar al paciente en su hogar?",
]

questions = map(lambda q: u"<span style=\"font-size: 1.2em; font-weight: bold; color: #333333;\">{0}</span>".format(q), questions)

# Texto con la explicacion de las escalas de la evaluacion funcional
func_scales = [
    (u"ocupaci\u00F3n", [
        u"0 = incapaz",
        u"1 = trabajo marginal solamente",
        u"2 = capacidad reducida respecto de lo normal",
        u"3 = normal"
    ]),
    (u"finanzas", [
        u"0 = incapaz",
        u"1 = harta asistencia",
        u"2 = poca asistencia",
        u"3 = normal"
    ]),
    (u"tareas dom\u00E9sticas", [
        u"0 = incapaz",
        u"1 = discapacitado",
        u"2 = normal"
    ]),
    (u"actividades de la vida diaria", [
        u"0 = cuidado total",
        u"1 = tareas gruesas \u00FAnicamente",
        u"2 = discapacidad m\u00EDnima",
        u"3 = normal"
    ]),
    (u"nivel de cuidado", [
        u"0 = cuidado profesional de tiempo completo",
        u"1 = cuidado en el hogar o cr\u00F3nico",
        u"2 = en el hogar"
    ])
]

fnames = map(lambda x: x[0], func_scales)
fscales = map(lambda x: u"<span style=\"color: #333333;\">{0}</span>".format("<br />".join(x[1])), func_scales)

class EvaluacionFuncional(models.Model, CSVExportable, PDFExportable):
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateField()
    # cuestionario
    opciones = (
        (u'Y', u'Si'),
        (u'N', u'No'),
        (u'E', u'No realizado'),
    )
    q1 = models.CharField(verbose_name="Q#1", help_text=questions[0], max_length=1, default='E', choices=opciones)
    q2 = models.CharField(verbose_name="Q#2", help_text=questions[1], max_length=1, default='E', choices=opciones)
    q3 = models.CharField(verbose_name="Q#3", help_text=questions[2], max_length=1, default='E', choices=opciones)
    q4 = models.CharField(verbose_name="Q#4", help_text=questions[3], max_length=1, default='E', choices=opciones)
    q5 = models.CharField(verbose_name="Q#5", help_text=questions[4], max_length=1, default='E', choices=opciones)
    q6 = models.CharField(verbose_name="Q#6", help_text=questions[5], max_length=1, default='E', choices=opciones)
    q7 = models.CharField(verbose_name="Q#7", help_text=questions[6], max_length=1, default='E', choices=opciones)
    q8 = models.CharField(verbose_name="Q#8", help_text=questions[7], max_length=1, default='E', choices=opciones)
    q9 = models.CharField(verbose_name="Q#9", help_text=questions[8], max_length=1, default='E', choices=opciones)
    q10 = models.CharField(verbose_name="Q#10", help_text=questions[9], max_length=1, default='E', choices=opciones)
    q11 = models.CharField(verbose_name="Q#11", help_text=questions[10], max_length=1, default='E', choices=opciones)
    q12 = models.CharField(verbose_name="Q#12", help_text=questions[11], max_length=1, default='E', choices=opciones)
    q13 = models.CharField(verbose_name="Q#13", help_text=questions[12], max_length=1, default='E', choices=opciones)
    q14 = models.CharField(verbose_name="Q#14", help_text=questions[13], max_length=1, default='E', choices=opciones)
    q15 = models.CharField(verbose_name="Q#15", help_text=questions[14], max_length=1, default='E', choices=opciones)
    q16 = models.CharField(verbose_name="Q#16", help_text=questions[15], max_length=1, default='E', choices=opciones)
    q17 = models.CharField(verbose_name="Q#17", help_text=questions[16], max_length=1, default='E', choices=opciones)
    q18 = models.CharField(verbose_name="Q#18", help_text=questions[17], max_length=1, default='E', choices=opciones)
    q19 = models.CharField(verbose_name="Q#19", help_text=questions[18], max_length=1, default='E', choices=opciones)
    q20 = models.CharField(verbose_name="Q#20", help_text=questions[19], max_length=1, default='E', choices=opciones)
    q21 = models.CharField(verbose_name="Q#21", help_text=questions[20], max_length=1, default='E', choices=opciones)
    q22 = models.CharField(verbose_name="Q#22", help_text=questions[21], max_length=1, default='E', choices=opciones)
    q23 = models.CharField(verbose_name="Q#23", help_text=questions[22], max_length=1, default='E', choices=opciones)
    q24 = models.CharField(verbose_name="Q#24", help_text=questions[23], max_length=1, default='E', choices=opciones)
    q25 = models.CharField(verbose_name="Q#25", help_text=questions[24], max_length=1, default='E', choices=opciones)
    # evaluacion de capacidad funcional
    choicevalues = map(lambda x: (x, str(x)), range(4))
    choices3 = tuple(choicevalues)
    choices2 = tuple(choicevalues[:-1])
    occupation = models.IntegerField(verbose_name=fnames[0], help_text=fscales[0], choices=choices3, blank=True, null=True)
    finances = models.IntegerField(verbose_name=fnames[1], help_text=fscales[1], choices=choices3, blank=True, null=True)
    chores = models.IntegerField(verbose_name=fnames[2], help_text=fscales[2], choices=choices2, blank=True, null=True)
    adl = models.IntegerField(verbose_name=fnames[3], help_text=fscales[3], choices=choices3, blank=True, null=True)
    care = models.IntegerField(verbose_name=fnames[4], help_text=fscales[4], choices=choices2, blank=True, null=True)

    def respuestas_cuestionario(self):
        # ugh
        return [getattr(self, "q{0}".format(i)) for i in range(1,26)]

    def respuestas_evaluacion(self):
        return [self.occupation, self.finances, self.chores, self.adl, self.care]

    def preguntas_efectuadas(self):
        return len(filter(lambda x: x != 'E', self.respuestas_cuestionario()))
    preguntas_efectuadas.short_description = u"n\u00B0 de preguntas"

    def porcentaje_respuestas_afirmativas(self):
        if self.preguntas_efectuadas() == 0:
            return "?"
        p = (100.0 * len(filter(lambda x: x == 'Y', self.respuestas_cuestionario()))) / self.preguntas_efectuadas()
        return ("%.1f" % p).replace(".", ",")
    porcentaje_respuestas_afirmativas.short_description = u"\u0025 de respuestas afirmativas"

    def total_capacidad_funcional(self):
        add_none = lambda a,b: a if b is None else a + b
        return reduce(add_none, self.respuestas_evaluacion(), 0)
    total_capacidad_funcional.short_description = u"puntaje total cap. funcional"

    def __unicode__(self):
        return u"eval. funcional de {0}".format(self.paciente)

    # Exportacion
    def get_csv_pairs(self):
        respuesta_verbose = lambda r: dict(self.opciones)[r]
        format_none = lambda x: "<en blanco>" if x is None else x
        pairs = [
            ("id paciente",                       self.paciente.pk),
            ("fecha",                             self.fecha),
            (u"num. de preguntas efectuadas",     self.preguntas_efectuadas()),
            (u"\u0025 de respuestas afirmativas", self.porcentaje_respuestas_afirmativas()),
            ("total puntaje capacidad func.",     self.total_capacidad_funcional())
        ]
        pairs = pairs + map(lambda x,y: (x,y), fnames, map(format_none, self.respuestas_evaluacion()))
        pairs = pairs + map(lambda x,y: (x,y), ["Q#{0}".format(i) for i in range(1,26)], map(respuesta_verbose, self.respuestas_cuestionario()))
        return pairs

    def get_pdf_pairs(self):
        return [
            (u"Evaluaci\u00F3n funcional",        self),
            (u"Fecha",                            self.fecha),
            (u"N\u00B0 de preguntas",             self.preguntas_efectuadas()),
            (u"\u0025 de respuestas afirmativas", self.porcentaje_respuestas_afirmativas()),
            (u"Puntaje total cap. funcional",     self.total_capacidad_funcional())
        ]

    class Meta:
        verbose_name = u'evaluaci\u00F3n funcional'
        verbose_name_plural = u'evaluaciones funcionales'

def get_file_path(instance, filename):
    return "neuroimagenes/{0}/{1}".format(instance.paciente.id, filename)

# Neuroimagenes de los pacientes, periodicas
class Neuroimagen(models.Model):
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to=get_file_path)
    def __unicode__(self):
        return u"neuroimagen de {0} - {1}".format(self.paciente, self.fecha)
    
    class Meta:
        verbose_name_plural = u'neuroim\u00E1genes'

# Otro examen periodico
class ExamenSignosVitales(models.Model, CSVExportable):
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateField()
    presion_arterial = models.IntegerField(verbose_name=u"presi\u00F3n arterial", help_text=u"presi\u00F3n arterial en [mm Hg]")
    pulso = models.IntegerField(verbose_name=u"pulso", help_text=u"pulso en [ppm]")
    altura = models.IntegerField(verbose_name=u"altura", help_text=u"altura en [cm]")
    peso = models.IntegerField(verbose_name=u"peso", help_text=u"peso en [kg]")

    def __unicode__(self):
        return "examen de signos vitales de {0}".format(self.paciente)

    def get_csv_pairs(self):
        return [
            (u"paciente (id)",         self.paciente.pk),
            (u"fecha",                 self.fecha.isoformat()),
            (u"presi\u00F3n arterial", self.presion_arterial),
            (u"pulso",                 self.pulso),
            (u"altura",                self.altura),
            (u"peso",                  self.peso)
        ]

    class Meta:
        verbose_name = u'examen de signos vitales'
        verbose_name_plural = u'ex\u00E1menes de signos vitales'

class ExamenFisico(models.Model, CSVExportable):
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateField()
    op = (
        (u'N', u"Normal"),
        (u'A', u"Anormal"),
        (u'E', u"No realizado"),
    )
    apariencia = models.CharField(verbose_name="apariencia general", max_length=1, choices=op, default='E')
    apariencia_glosa = models.TextField(verbose_name=u"descripci\u00F3n de apariencia general", max_length=1000, blank=True)
    piel = models.CharField(max_length=1, choices=op, default='E')
    piel_glosa = models.TextField(verbose_name=u"descripci\u00F3n de piel", max_length=1000, blank=True)
    cabeza = models.CharField(verbose_name=u"cabeza - cuello", max_length=1, choices=op, default='E')
    cabeza_glosa = models.TextField(verbose_name=u"descripci\u00F3n de cabeza - cuello", max_length=1000, blank=True)
    ojos = models.CharField(verbose_name=u"ojos - orejas - nariz - garganta", max_length=1, choices=op, default='E')
    ojos_glosa = models.TextField(verbose_name=u"descripci\u00F3n de ojos - orejas - nariz - garganta", max_length=1000, blank=True)
    pecho = models.CharField(verbose_name=u"pulmones - pecho", max_length=1, choices=op, default='E')
    pecho_glosa = models.TextField(verbose_name=u"descripci\u00F3n de pulmones - pecho", max_length=1000, blank=True)
    corazon = models.CharField(verbose_name=u"coraz\u00F3n", max_length=1, choices=op, default='E')
    corazon_glosa = models.TextField(verbose_name=u"descripci\u00F3n de coraz\u00F3n", max_length=1000, blank=True)
    abdomen = models.CharField(max_length=1, choices=op, default='E')
    abdomen_glosa = models.TextField(verbose_name=u"descripci\u00F3n de abdomen", max_length=1000, blank=True)
    extremidades = models.CharField(max_length=1, choices=op, default='E')
    extremidades_glosa = models.TextField(verbose_name=u"descripci\u00F3n de extremidades", max_length=1000, blank=True)

    def __unicode__(self):
        return u"examen f\u00EDsico de {0}".format(self.paciente)

    def get_csv_pairs(self):
        con_glosa = lambda attr: dict(self.op)[getattr(self,attr)] if getattr(self,attr) != u'A' else "Anormal - " + getattr(self,attr + "_glosa")
        return [
            (u"paciente (id)",                    self.paciente.pk),
            (u"fecha",                            self.fecha.isoformat()),
            (u"apariencia general",               con_glosa("apariencia")),
            (u"piel",                             con_glosa("piel")),
            (u"cabeza - cuello",                  con_glosa("cabeza")),
            (u"ojos - orejas - nariz - garganta", con_glosa("ojos")),
            (u"pulmones - pecho",                 con_glosa("pecho")),
            (u"coraz\u00F3n",                     con_glosa("corazon")),
            (u"abdomen",                          con_glosa("abdomen")),
            (u"extremidades",                     con_glosa("extremidades"))
        ]

    class Meta:
        verbose_name = u'examen f\u00EDsico'
        verbose_name_plural = u'ex\u00E1menes f\u00EDsicos'

class ExamenNeurologico(models.Model, CSVExportable):
    paciente = models.ForeignKey(Paciente)
    fecha = models.DateField()
    op = (
        (u'N', u"Normal"),
        (u'A', u"Anormal"),
        (u'E', u"No realizado"),
    )
    estado_mental = models.CharField(verbose_name=u"estado mental", max_length=1, choices=op, default='E')
    estado_mental_glosa = models.TextField(verbose_name=u"descripci\u00F3n de estado mental", max_length=1000, blank=True)
    nervios_craneales = models.CharField(verbose_name=u"nervios craneales", max_length=1, choices=op, default='E')
    nervios_craneales_glosa = models.TextField(verbose_name=u"descripci\u00F3n de nervios craneales", max_length=1000, blank=True)
    sistema_motor = models.CharField(verbose_name=u"sistema motor", max_length=1, choices=op, default='E')
    sistema_motor_glosa = models.TextField(verbose_name=u"descripci\u00F3n de sistema motor", max_length=1000, blank=True)
    sistema_sensorial = models.CharField(verbose_name=u"sistema sensorial", max_length=1, choices=op, default='E')
    sistema_sensorial_glosa = models.TextField(verbose_name=u"descripci\u00F3n de sistema sensorial", max_length=1000, blank=True)
    reflejos = models.CharField(verbose_name=u"reflejos", max_length=1, choices=op, default='E')
    reflejos_glosa = models.TextField(verbose_name=u"descripci\u00F3n de reflejos", max_length=1000, blank=True)
    coordinacion = models.CharField(verbose_name=u"coordinaci\u00F3n", max_length=1, choices=op, default='E')
    coordinacion_glosa = models.TextField(verbose_name=u"descripci\u00F3n de coordinaci\u00F3n", max_length=1000, blank=True)

    def __unicode__(self):
        return u"examen neurol\u00F3gico de {0}".format(self.paciente)

    def get_csv_pairs(self):
        con_glosa = lambda attr: dict(self.op)[getattr(self,attr)] if getattr(self,attr) != u'A' else "Anormal - " + getattr(self,attr + "_glosa")
        return [
            (u"paciente (id)",     self.paciente.pk),
            (u"fecha",             self.fecha.isoformat()),
            (u"estado mental",     con_glosa("estado_mental")),
            (u"nervios craneales", con_glosa("nervios_craneales")),
            (u"sistema motor",     con_glosa("sistema_motor")),
            (u"sistema sensorial", con_glosa("sistema_sensorial")),
            (u"reflejos",          con_glosa("reflejos")),
            (u"coordinaci\u00F3n", con_glosa("coordinacion"))
        ]

    class Meta:
        verbose_name = u'examen neurol\u00F3gico'
        verbose_name_plural = u'ex\u00E1menes neurol\u00F3gicos'

