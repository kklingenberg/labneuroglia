--
-- PostgreSQL database dump
--

SET client_encoding = 'UTF8';
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: laboratorio; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE laboratorio WITH TEMPLATE = template0 ENCODING = 'UTF8';


ALTER DATABASE laboratorio OWNER TO postgres;

\connect laboratorio

SET client_encoding = 'UTF8';
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'Standard public schema';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group (
    id serial NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('auth_group', 'id'), 5, true);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id serial NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('auth_group_permissions', 'id'), 114, true);


--
-- Name: auth_message; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_message (
    id serial NOT NULL,
    user_id integer NOT NULL,
    message text NOT NULL
);


ALTER TABLE public.auth_message OWNER TO postgres;

--
-- Name: auth_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('auth_message', 'id'), 1, false);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_permission (
    id serial NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('auth_permission', 'id'), 81, true);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user (
    id serial NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    "password" character varying(128) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id serial NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('auth_user_groups', 'id'), 33, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('auth_user', 'id'), 12, true);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id serial NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('auth_user_user_permissions', 'id'), 2, true);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_admin_log (
    id serial NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('django_admin_log', 'id'), 59, true);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_content_type (
    id serial NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('django_content_type', 'id'), 27, true);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE django_site (
    id serial NOT NULL,
    "domain" character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('django_site', 'id'), 1, true);


--
-- Name: pacientes_evaluacionfuncional; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pacientes_evaluacionfuncional (
    id serial NOT NULL,
    paciente_id integer NOT NULL,
    fecha date NOT NULL,
    q1 character varying(1) NOT NULL,
    q2 character varying(1) NOT NULL,
    q3 character varying(1) NOT NULL,
    q4 character varying(1) NOT NULL,
    q5 character varying(1) NOT NULL,
    q6 character varying(1) NOT NULL,
    q7 character varying(1) NOT NULL,
    q8 character varying(1) NOT NULL,
    q9 character varying(1) NOT NULL,
    q10 character varying(1) NOT NULL,
    q11 character varying(1) NOT NULL,
    q12 character varying(1) NOT NULL,
    q13 character varying(1) NOT NULL,
    q14 character varying(1) NOT NULL,
    q15 character varying(1) NOT NULL,
    q16 character varying(1) NOT NULL,
    q17 character varying(1) NOT NULL,
    q18 character varying(1) NOT NULL,
    q19 character varying(1) NOT NULL,
    q20 character varying(1) NOT NULL,
    q21 character varying(1) NOT NULL,
    q22 character varying(1) NOT NULL,
    q23 character varying(1) NOT NULL,
    q24 character varying(1) NOT NULL,
    q25 character varying(1) NOT NULL,
    occupation integer,
    finances integer,
    chores integer,
    adl integer,
    care integer
);


ALTER TABLE public.pacientes_evaluacionfuncional OWNER TO postgres;

--
-- Name: pacientes_evaluacionfuncional_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('pacientes_evaluacionfuncional', 'id'), 1, false);


--
-- Name: pacientes_evaluacionmotora; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pacientes_evaluacionmotora (
    id serial NOT NULL,
    paciente_id integer NOT NULL,
    fecha date NOT NULL,
    ocular_pursuit integer,
    saccade_initiation integer,
    saccade_velocity integer,
    dysarthria integer,
    tongue_protrusion integer,
    maximal_dystonia integer,
    maximal_chorea integer,
    retropulsion_pull_test integer,
    finger_taps integer,
    pronate_supinate_hands integer,
    luria integer,
    rigidity_arms integer,
    bradykinesia_body integer,
    gait integer,
    tandem_walking integer
);


ALTER TABLE public.pacientes_evaluacionmotora OWNER TO postgres;

--
-- Name: pacientes_evaluacionmotora_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('pacientes_evaluacionmotora', 'id'), 1, false);


--
-- Name: pacientes_examenfisico; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pacientes_examenfisico (
    id serial NOT NULL,
    paciente_id integer NOT NULL,
    fecha date NOT NULL,
    apariencia character varying(1) NOT NULL,
    apariencia_glosa text NOT NULL,
    piel character varying(1) NOT NULL,
    piel_glosa text NOT NULL,
    cabeza character varying(1) NOT NULL,
    cabeza_glosa text NOT NULL,
    ojos character varying(1) NOT NULL,
    ojos_glosa text NOT NULL,
    pecho character varying(1) NOT NULL,
    pecho_glosa text NOT NULL,
    corazon character varying(1) NOT NULL,
    corazon_glosa text NOT NULL,
    abdomen character varying(1) NOT NULL,
    abdomen_glosa text NOT NULL,
    extremidades character varying(1) NOT NULL,
    extremidades_glosa text NOT NULL
);


ALTER TABLE public.pacientes_examenfisico OWNER TO postgres;

--
-- Name: pacientes_examenfisico_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('pacientes_examenfisico', 'id'), 1, false);


--
-- Name: pacientes_examenneurologico; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pacientes_examenneurologico (
    id serial NOT NULL,
    paciente_id integer NOT NULL,
    fecha date NOT NULL,
    estado_mental character varying(1) NOT NULL,
    estado_mental_glosa text NOT NULL,
    nervios_craneales character varying(1) NOT NULL,
    nervios_craneales_glosa text NOT NULL,
    sistema_motor character varying(1) NOT NULL,
    sistema_motor_glosa text NOT NULL,
    sistema_sensorial character varying(1) NOT NULL,
    sistema_sensorial_glosa text NOT NULL,
    reflejos character varying(1) NOT NULL,
    reflejos_glosa text NOT NULL,
    coordinacion character varying(1) NOT NULL,
    coordinacion_glosa text NOT NULL
);


ALTER TABLE public.pacientes_examenneurologico OWNER TO postgres;

--
-- Name: pacientes_examenneurologico_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('pacientes_examenneurologico', 'id'), 1, false);


--
-- Name: pacientes_examensignosvitales; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pacientes_examensignosvitales (
    id serial NOT NULL,
    paciente_id integer NOT NULL,
    fecha date NOT NULL,
    presion_arterial integer NOT NULL,
    pulso integer NOT NULL,
    altura integer NOT NULL,
    peso integer NOT NULL
);


ALTER TABLE public.pacientes_examensignosvitales OWNER TO postgres;

--
-- Name: pacientes_examensignosvitales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('pacientes_examensignosvitales', 'id'), 1, false);


--
-- Name: pacientes_familiar; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pacientes_familiar (
    id serial NOT NULL,
    paciente_id integer NOT NULL,
    parentesco character varying(50) NOT NULL
);


ALTER TABLE public.pacientes_familiar OWNER TO postgres;

--
-- Name: pacientes_familiar_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('pacientes_familiar', 'id'), 1, false);


--
-- Name: pacientes_neuroimagen; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pacientes_neuroimagen (
    id serial NOT NULL,
    paciente_id integer NOT NULL,
    fecha date NOT NULL,
    imagen character varying(100) NOT NULL
);


ALTER TABLE public.pacientes_neuroimagen OWNER TO postgres;

--
-- Name: pacientes_neuroimagen_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('pacientes_neuroimagen', 'id'), 1, false);


--
-- Name: pacientes_paciente; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pacientes_paciente (
    id serial NOT NULL,
    sexo character varying(1) NOT NULL,
    nacimiento date NOT NULL,
    raza character varying(30) NOT NULL,
    raza_otro character varying(40) NOT NULL,
    test_genetico character varying(1) NOT NULL,
    tripletes integer NOT NULL,
    fecha_consentimiento date,
    fecha_diagnostico date,
    fecha_sintomas date,
    fecha_tratamiento date,
    medicacion character varying(1) NOT NULL,
    medicacion_glosa text NOT NULL,
    enfermedades_pasadas character varying(1) NOT NULL,
    enfermedades_pasadas_glosa text NOT NULL,
    cirugias character varying(1) NOT NULL,
    cirugias_glosa text NOT NULL
);


ALTER TABLE public.pacientes_paciente OWNER TO postgres;

--
-- Name: pacientes_paciente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('pacientes_paciente', 'id'), 1, false);


--
-- Name: viales_linea; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE viales_linea (
    id serial NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion text NOT NULL
);


ALTER TABLE public.viales_linea OWNER TO postgres;

--
-- Name: viales_linea_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('viales_linea', 'id'), 7, true);


--
-- Name: viales_stock; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE viales_stock (
    id serial NOT NULL,
    nombre character varying(100) NOT NULL,
    descripcion text NOT NULL
);


ALTER TABLE public.viales_stock OWNER TO postgres;

--
-- Name: viales_stock_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('viales_stock', 'id'), 1, true);


--
-- Name: viales_vial; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE viales_vial (
    id serial NOT NULL,
    ubicacion character varying(20) NOT NULL,
    fecha date NOT NULL,
    linea_id integer NOT NULL,
    stock_id integer NOT NULL,
    vigente character varying(1) NOT NULL,
    observaciones text NOT NULL,
    usuario_id integer NOT NULL,
    descongelacion date,
    usuario_descongela_id integer
);


ALTER TABLE public.viales_vial OWNER TO postgres;

--
-- Name: viales_vial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('viales_vial', 'id'), 1, true);


--
-- Name: vivero_genotipo; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vivero_genotipo (
    id serial NOT NULL,
    genotipo character varying(100) NOT NULL
);


ALTER TABLE public.vivero_genotipo OWNER TO postgres;

--
-- Name: vivero_genotipo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('vivero_genotipo', 'id'), 2, true);


--
-- Name: vivero_historico; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vivero_historico (
    id serial NOT NULL,
    raton_id integer NOT NULL,
    instante timestamp with time zone NOT NULL,
    estado character varying(1) NOT NULL,
    evento character varying(30) NOT NULL,
    usuario_id integer
);


ALTER TABLE public.vivero_historico OWNER TO postgres;

--
-- Name: vivero_historico_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('vivero_historico', 'id'), 6, true);


--
-- Name: vivero_imagenraton; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vivero_imagenraton (
    id serial NOT NULL,
    raton_id integer NOT NULL,
    imagen character varying(100) NOT NULL,
    fecha date NOT NULL,
    descripcion text NOT NULL
);


ALTER TABLE public.vivero_imagenraton OWNER TO postgres;

--
-- Name: vivero_imagenraton_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('vivero_imagenraton', 'id'), 1, true);


--
-- Name: vivero_linea; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vivero_linea (
    id serial NOT NULL,
    linea character varying(100) NOT NULL
);


ALTER TABLE public.vivero_linea OWNER TO postgres;

--
-- Name: vivero_linea_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('vivero_linea', 'id'), 1, true);


--
-- Name: vivero_raton; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vivero_raton (
    id serial NOT NULL,
    linea_id integer NOT NULL,
    camada character varying(100) NOT NULL,
    numero integer NOT NULL,
    sexo character varying(1) NOT NULL,
    genotipo_id integer NOT NULL,
    regenotipo_id integer NOT NULL,
    nacimiento date NOT NULL,
    colonia character varying(100) NOT NULL,
    estado character varying(1) NOT NULL,
    muerte date,
    observaciones text NOT NULL,
    padre_id integer,
    madre_id integer
);


ALTER TABLE public.vivero_raton OWNER TO postgres;

--
-- Name: vivero_raton_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('vivero_raton', 'id'), 2, true);


--
-- Name: vivero_reserva; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vivero_reserva (
    id serial NOT NULL,
    raton_id integer NOT NULL,
    usuario_id integer NOT NULL,
    tipo character varying(1) NOT NULL,
    fecha date NOT NULL,
    fecha_termino date,
    creada timestamp with time zone NOT NULL,
    observaciones text NOT NULL
);


ALTER TABLE public.vivero_reserva OWNER TO postgres;

--
-- Name: vivero_reserva_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('vivero_reserva', 'id'), 1, true);


--
-- Name: vivero_revision; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vivero_revision (
    id serial NOT NULL,
    raton_id integer NOT NULL,
    fecha date NOT NULL,
    peso integer NOT NULL,
    aspecto text NOT NULL,
    aspecto_puntaje integer NOT NULL,
    comportamiento text NOT NULL,
    comportamiento_puntaje integer NOT NULL,
    signos text NOT NULL,
    signos_puntaje integer NOT NULL,
    constantes text NOT NULL,
    constantes_puntaje integer NOT NULL
);


ALTER TABLE public.vivero_revision OWNER TO postgres;

--
-- Name: vivero_revision_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('vivero_revision', 'id'), 1, true);


--
-- Name: vivero_videoraton; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vivero_videoraton (
    id serial NOT NULL,
    raton_id integer NOT NULL,
    video character varying(100) NOT NULL,
    fecha date NOT NULL,
    descripcion text NOT NULL
);


ALTER TABLE public.vivero_videoraton OWNER TO postgres;

--
-- Name: vivero_videoraton_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval(pg_catalog.pg_get_serial_sequence('vivero_videoraton', 'id'), 1, false);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
1	veterinario
2	superusuarios lab
3	superusuarios pacientes
4	superusuarios viales
5	equipo lab
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	43
2	1	44
3	1	45
4	2	31
5	2	32
6	2	33
7	2	34
8	2	35
9	2	36
10	2	37
11	2	38
12	2	39
13	2	40
14	2	41
15	2	42
16	2	43
17	2	44
18	2	45
19	2	46
20	2	47
21	2	48
22	2	49
23	2	50
24	2	51
25	2	52
26	2	53
27	2	54
28	3	55
29	3	56
30	3	57
31	3	58
32	3	59
33	3	60
34	3	61
35	3	62
36	3	63
37	3	64
38	3	65
39	3	66
40	3	67
41	3	68
42	3	69
43	3	70
44	3	71
45	3	72
46	3	73
47	3	74
48	3	75
49	3	76
50	3	77
51	3	78
52	4	22
53	4	23
54	4	24
55	4	25
56	4	26
57	4	27
58	4	28
59	4	29
60	4	30
102	5	34
103	5	37
104	5	38
105	5	40
106	5	41
107	5	46
108	5	47
109	5	48
110	5	49
111	5	50
112	5	51
113	5	28
114	5	29
\.


--
-- Data for Name: auth_message; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_message (id, user_id, message) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add message	4	add_message
11	Can change message	4	change_message
12	Can delete message	4	delete_message
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add site	7	add_site
20	Can change site	7	change_site
21	Can delete site	7	delete_site
22	Can add stock	8	add_stock
23	Can change stock	8	change_stock
24	Can delete stock	8	delete_stock
25	Can add línea celular	9	add_linea
26	Can change línea celular	9	change_linea
27	Can delete línea celular	9	delete_linea
28	Can add vial	10	add_vial
29	Can change vial	10	change_vial
30	Can delete vial	10	delete_vial
31	Can add línea genética	11	add_linea
32	Can change línea genética	11	change_linea
33	Can delete línea genética	11	delete_linea
34	Can add genotipo	12	add_genotipo
35	Can change genotipo	12	change_genotipo
36	Can delete genotipo	12	delete_genotipo
37	Can add ratón	13	add_raton
38	Can change ratón	13	change_raton
39	Can delete ratón	13	delete_raton
40	Can add reserva	14	add_reserva
41	Can change reserva	14	change_reserva
42	Can delete reserva	14	delete_reserva
43	Can add revisión veterinaria	15	add_revision
44	Can change revisión veterinaria	15	change_revision
45	Can delete revisión veterinaria	15	delete_revision
46	Can add imagen	16	add_imagenraton
47	Can change imagen	16	change_imagenraton
48	Can delete imagen	16	delete_imagenraton
49	Can add videos	17	add_videoraton
50	Can change videos	17	change_videoraton
51	Can delete videos	17	delete_videoraton
52	Can add historico	18	add_historico
53	Can change historico	18	change_historico
54	Can delete historico	18	delete_historico
55	Can add paciente	19	add_paciente
56	Can change paciente	19	change_paciente
57	Can delete paciente	19	delete_paciente
58	Can add familiar	20	add_familiar
59	Can change familiar	20	change_familiar
60	Can delete familiar	20	delete_familiar
61	Can add evaluación motora	21	add_evaluacionmotora
62	Can change evaluación motora	21	change_evaluacionmotora
63	Can delete evaluación motora	21	delete_evaluacionmotora
64	Can add evaluación funcional	22	add_evaluacionfuncional
65	Can change evaluación funcional	22	change_evaluacionfuncional
66	Can delete evaluación funcional	22	delete_evaluacionfuncional
67	Can add neuroimagen	23	add_neuroimagen
68	Can change neuroimagen	23	change_neuroimagen
69	Can delete neuroimagen	23	delete_neuroimagen
70	Can add examen de signos vitales	24	add_examensignosvitales
71	Can change examen de signos vitales	24	change_examensignosvitales
72	Can delete examen de signos vitales	24	delete_examensignosvitales
73	Can add examen físico	25	add_examenfisico
74	Can change examen físico	25	change_examenfisico
75	Can delete examen físico	25	delete_examenfisico
76	Can add examen neurológico	26	add_examenneurologico
77	Can change examen neurológico	26	change_examenneurologico
78	Can delete examen neurológico	26	delete_examenneurologico
79	Can add log entry	27	add_logentry
80	Can change log entry	27	change_logentry
81	Can delete log entry	27	delete_logentry
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, username, first_name, last_name, email, "password", is_staff, is_active, is_superuser, last_login, date_joined) FROM stdin;
6	Magda				sha1$ac952$e3cdf5682e712eeb0b1ec13175cb031f5c007a02	t	t	f	2011-12-29 11:08:39-03	2011-12-29 11:08:39-03
10	Ale				sha1$855f8$e3baef975ed2213db69b83965700003791efc895	t	t	f	2011-12-29 11:11:48-03	2011-12-29 11:11:48-03
7	Felipe				sha1$482be$1d60d8aeac953da09f32f6d85badbabe092cdd54	t	t	f	2011-12-29 11:15:23.344865-03	2011-12-29 11:09:15-03
9	Carlos				sha1$e0eb0$809e3e54b6d4185e276a54bc9f27b3ac734e2715	t	t	f	2011-12-29 19:46:18.25192-03	2011-12-29 11:11:32-03
2	maite	Maite	Castro	maitecastro@gmail.com	sha1$64435$2cd73ea7950c1baa3ef952186af7a0d3ad982f19	t	t	f	2011-12-29 20:12:57.4592-03	2011-12-26 15:47:21-03
4	Paxi	Maria Paz			sha1$8f75d$5fbde243043e54974ad25186afb862281c2f00a7	t	t	f	2011-12-29 20:34:34.853471-03	2011-12-29 10:40:21-03
11	Pablo				sha1$4b776$b9c28fdc6acf33d27efab11b82332dbe1212c884	t	t	f	2011-12-29 21:47:16.383202-03	2011-12-29 11:12:26-03
12	Pau				sha1$28f63$ce6ee1d8c21cb30c8621cdd022b89cfb0b2d9469	t	t	f	2011-12-30 12:51:09.353791-03	2011-12-29 11:13:12-03
8	Maca				sha1$3f066$ed915a33d567796c6b274d3d4d362c32520f0582	t	t	f	2012-01-01 20:05:02.830309-03	2011-12-29 11:09:56-03
5	Anibal				sha1$76e8c$c91ff942028030be46cb4d39e663e5e0e91c8846	t	t	f	2012-01-06 14:38:17.772906-03	2011-12-29 11:08:09-03
3	cjuri	Carlos	Juri	cajuri@gmail.com	sha1$61578$f1d3aa3acb3b64003df6f02dc03ee642e0318142	t	t	f	2012-01-06 18:06:00.490091-03	2011-12-26 15:48:38-03
1	laboratorio	Kai	Klingenberg	k.klingenberg@gmail.com	sha1$06496$de49612cf2e4062330d893ada064448b139b935f	t	t	t	2012-01-13 15:42:04.670456-03	2011-12-24 16:30:27-03
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
4	3	3
5	2	2
6	2	3
7	2	4
10	4	4
11	4	5
25	12	5
26	11	5
27	6	5
28	8	5
29	7	2
30	7	5
31	9	5
32	5	5
33	10	5
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
1	2	8
2	2	7
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2011-12-24 17:06:16.29774-03	1	7	1	labneuroglia.uach.cl	2	Modificado/a domain y name.
2	2011-12-24 17:32:21.583554-03	1	12	1	homocigoto	1	
3	2011-12-24 17:32:33.043681-03	1	11	1	blanco	1	
4	2011-12-24 17:35:23.084977-03	1	13	2	camada a; número 1	1	
5	2011-12-26 15:40:20.820604-03	1	2	1	veterinario	1	
6	2011-12-26 15:42:01.429264-03	1	2	2	superusuarios lab	1	
7	2011-12-26 15:43:01.763512-03	1	2	3	superusuarios pacientes	1	
8	2011-12-26 15:44:00.439964-03	1	2	4	superusuarios viales	1	
9	2011-12-26 15:46:37.40071-03	1	2	5	equipo lab	1	
10	2011-12-26 15:47:21.719465-03	1	3	2	maite	1	
11	2011-12-26 15:48:10.651297-03	1	3	2	maite	2	Modificado/a first_name, last_name, email, is_staff y groups.
12	2011-12-26 15:48:38.357692-03	1	3	3	cjuri	1	
13	2011-12-26 15:49:00.352545-03	1	3	3	cjuri	2	Modificado/a first_name, last_name, email, is_staff y groups.
14	2011-12-28 22:08:27.534393-03	1	9	1	C6 shRNA GLUT1	1	
15	2011-12-28 22:08:38.282562-03	1	9	2	C6 shRNA GLUT3	1	
16	2011-12-28 22:09:02.773185-03	1	9	3	Hdh Q111	1	
17	2011-12-28 22:09:17.31476-03	1	9	4	Hdh Q07	1	
18	2011-12-28 22:09:25.413845-03	1	9	5	C6	1	
19	2011-12-28 22:09:37.108338-03	1	9	6	HEK293T	1	
20	2011-12-28 22:09:49.706934-03	1	9	7	NG108	1	
21	2011-12-28 22:10:19.870283-03	1	8	1	Tanque de nitrógeno	1	
22	2011-12-29 10:36:51.775073-03	1	3	2	maite	2	Modificado/a user_permissions.
23	2011-12-29 10:40:21.800913-03	2	3	4	Paxi	1	
24	2011-12-29 10:42:24.412025-03	2	3	4	Paxi	2	Modificado/a first_name, is_staff y groups.
25	2011-12-29 11:05:04.74324-03	1	3	4	Paxi	2	Modificado/a first_name.
26	2011-12-29 11:08:09.251652-03	1	3	5	anibal	1	
27	2011-12-29 11:08:25.226203-03	1	3	5	anibal	2	Modificado/a first_name, last_name, is_staff y groups.
28	2011-12-29 11:08:39.552431-03	1	3	6	magda	1	
29	2011-12-29 11:08:51.832144-03	1	3	6	magda	2	Modificado/a first_name, is_staff y groups.
30	2011-12-29 11:09:15.967978-03	1	3	7	felipe	1	
31	2011-12-29 11:09:43.935894-03	1	3	7	felipe	2	Modificado/a first_name, last_name, is_staff y groups.
32	2011-12-29 11:09:56.788279-03	1	3	8	maca	1	
33	2011-12-29 11:10:15.200625-03	1	3	8	maca	2	Modificado/a is_staff y groups.
34	2011-12-29 11:10:35.22661-03	1	3	7	felipe	2	Modificado/a groups.
35	2011-12-29 11:10:46.334548-03	1	3	6	magda	2	Modificado/a first_name.
36	2011-12-29 11:10:56.173642-03	1	3	7	felipe	2	Modificado/a first_name y last_name.
37	2011-12-29 11:11:02.627239-03	1	3	5	anibal	2	Modificado/a first_name y last_name.
38	2011-12-29 11:11:32.808174-03	1	3	9	carlos	1	
39	2011-12-29 11:11:39.469175-03	1	3	9	carlos	2	Modificado/a is_staff y groups.
40	2011-12-29 11:11:48.74176-03	1	3	10	ale	1	
41	2011-12-29 11:11:58.932332-03	1	3	10	ale	2	Modificado/a is_staff y groups.
42	2011-12-29 11:12:26.608217-03	1	3	11	pablo	1	
43	2011-12-29 11:12:32.881665-03	1	3	11	pablo	2	Modificado/a is_staff y groups.
44	2011-12-29 11:13:12.745292-03	1	3	12	Pau	1	
45	2011-12-29 11:13:19.543639-03	1	3	12	Pau	2	Modificado/a is_staff y groups.
46	2011-12-29 11:13:43.484133-03	1	3	11	Pablo	2	Modificado/a username.
47	2011-12-29 11:13:54.469081-03	1	3	6	Magda	2	Modificado/a username.
48	2011-12-29 11:14:03.792048-03	1	3	8	Maca	2	Modificado/a username.
49	2011-12-29 11:14:12.025708-03	1	3	7	Felipe	2	Modificado/a username.
50	2011-12-29 11:14:19.27044-03	1	3	9	Carlos	2	Modificado/a username.
51	2011-12-29 11:14:27.373766-03	1	3	5	Anibal	2	Modificado/a username.
52	2011-12-29 11:14:33.075095-03	1	3	10	Ale	2	Modificado/a username.
53	2011-12-29 11:14:54.728158-03	1	3	1	laboratorio	2	Modificado/a first_name y last_name.
54	2011-12-29 11:18:57.060541-03	1	2	5	equipo lab	2	Modificado/a permissions.
55	2011-12-29 11:20:26.854767-03	1	2	5	equipo lab	2	Modificado/a permissions.
56	2011-12-29 11:20:57.925717-03	1	15	1	revisión de ratón<camada a; número 1>	1	
57	2011-12-29 11:22:05.150724-03	12	12	2	heterocigoto	1	
58	2011-12-29 19:44:20.947352-03	5	10	1	vial E1 de línea HEK293T	1	
59	2011-12-29 20:35:53.924454-03	4	9	5	C6	2	No ha cambiado ningún campo.
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	message	auth	message
5	content type	contenttypes	contenttype
6	session	sessions	session
7	site	sites	site
8	stock	viales	stock
9	línea celular	viales	linea
10	vial	viales	vial
11	línea genética	vivero	linea
12	genotipo	vivero	genotipo
13	ratón	vivero	raton
14	reserva	vivero	reserva
15	revisión veterinaria	vivero	revision
16	imagen	vivero	imagenraton
17	videos	vivero	videoraton
18	historico	vivero	historico
19	paciente	pacientes	paciente
20	familiar	pacientes	familiar
21	evaluación motora	pacientes	evaluacionmotora
22	evaluación funcional	pacientes	evaluacionfuncional
23	neuroimagen	pacientes	neuroimagen
24	examen de signos vitales	pacientes	examensignosvitales
25	examen físico	pacientes	examenfisico
26	examen neurológico	pacientes	examenneurologico
27	log entry	admin	logentry
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
660d88fbc57e8f4ddd42bef702a6c94a	MzIyYmQ1NGZhMDkyODJiYjFjYTMxOTgwMmQyMGYyZTQ1Njc4NWVmZjqAAn1xAS4=\n	2012-01-07 17:07:33.276927-03
0fcfa514e2712c6942192760107c4bd0	NTgyYjRmYzVlMmYyYWFkODFlMzJjNDI1NzI2NTQ0NGJmMTQzZWJmOTqAAn1xAVUKdGVzdGNvb2tp\nZVUGd29ya2VkcQJzLg==\n	2012-01-07 18:30:03.983056-03
f294bb0808d07101da1eae953e4b08f5	YWZjYjgxMmE2ODBlYTJiNzI2OTIyMjU2MjRiZmYxZmQ1NzRmMDJkNjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n	2012-01-09 08:51:06.000959-03
277e28dc456db264d9976399a6dd127b	YWZjYjgxMmE2ODBlYTJiNzI2OTIyMjU2MjRiZmYxZmQ1NzRmMDJkNjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n	2012-01-09 08:53:26.684349-03
a76c58bca80f6bc7328ca74b6ffc59d3	MzIyYmQ1NGZhMDkyODJiYjFjYTMxOTgwMmQyMGYyZTQ1Njc4NWVmZjqAAn1xAS4=\n	2012-01-09 17:23:06.183833-03
b899c884c151030c16b821abcc5de84b	ZWY4NjAzNzQ3MWE3MGE5NTJmMjQzZjMwNzUwMDM5MDcwNzBmNjZlMzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRLAnUu\n	2012-01-12 10:37:03.384703-03
b0ceeddcf1ac1053abcd04133808f76b	NjlhMjU3YmU2M2UyNjg2Njk2YmVjMjJlMzk2OGNiYmJjNTI0MzI2YTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRLCXUu\n	2012-01-12 19:46:18.260719-03
89bacbb88d05901b7c77fc5af1593419	ZWY4NjAzNzQ3MWE3MGE5NTJmMjQzZjMwNzUwMDM5MDcwNzBmNjZlMzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRLAnUu\n	2012-01-12 20:12:57.46652-03
91e7cbad2947735853a51c1314d454be	MzIyYmQ1NGZhMDkyODJiYjFjYTMxOTgwMmQyMGYyZTQ1Njc4NWVmZjqAAn1xAS4=\n	2012-01-12 20:36:38.958637-03
47cbf106f903fdbc85631b9d0b06f549	MzIyYmQ1NGZhMDkyODJiYjFjYTMxOTgwMmQyMGYyZTQ1Njc4NWVmZjqAAn1xAS4=\n	2012-01-12 21:47:52.066398-03
c35633726d823b32169a340f0cfa054e	NTExMjI4YjZmZmI4M2I2MjE1MTI2OWY5ZjRjNjRkYTZmN2E5MDAzNjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRLDHUu\n	2012-01-13 12:51:09.362683-03
a3e48a88d1d49199f5ce0e0310b3926f	MzIyYmQ1NGZhMDkyODJiYjFjYTMxOTgwMmQyMGYyZTQ1Njc4NWVmZjqAAn1xAS4=\n	2012-01-15 20:05:19.48923-03
fde233268c34ab8253deba200af8ebad	YWZjYjgxMmE2ODBlYTJiNzI2OTIyMjU2MjRiZmYxZmQ1NzRmMDJkNjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n	2012-01-18 16:11:36.764569-03
d73bc6629e1c2bae3f3d5479fbbf9d40	Yzc2NWI4YjQ4ZjQ2ZjcyMWZmNzQxYzcxZmQwZWVlZmJiYzNiYjMzODqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxAlUN\nX2F1dGhfdXNlcl9pZEsFdS4=\n	2012-01-20 14:38:17.785935-03
962d30ff4a21c5ab2623e05e7399a0ea	ODI3Njc0NTIxNjQ3MzgxMThlZjFmNDRhZWIwZDdiZDllY2EyMDM3ZjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRLAXUu\n	2012-01-20 18:06:25.25883-03
afd34c201379110544658aea99ac7e66	YWZjYjgxMmE2ODBlYTJiNzI2OTIyMjU2MjRiZmYxZmQ1NzRmMDJkNjqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n	2012-01-26 12:27:22.23915-03
b6bf99fd31f080511201ec162398e790	ODI3Njc0NTIxNjQ3MzgxMThlZjFmNDRhZWIwZDdiZDllY2EyMDM3ZjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRLAXUu\n	2012-01-27 15:42:04.677903-03
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_site (id, "domain", name) FROM stdin;
1	labneuroglia.uach.cl	labneuroglia.uach.cl
\.


--
-- Data for Name: pacientes_evaluacionfuncional; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pacientes_evaluacionfuncional (id, paciente_id, fecha, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, occupation, finances, chores, adl, care) FROM stdin;
\.


--
-- Data for Name: pacientes_evaluacionmotora; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pacientes_evaluacionmotora (id, paciente_id, fecha, ocular_pursuit, saccade_initiation, saccade_velocity, dysarthria, tongue_protrusion, maximal_dystonia, maximal_chorea, retropulsion_pull_test, finger_taps, pronate_supinate_hands, luria, rigidity_arms, bradykinesia_body, gait, tandem_walking) FROM stdin;
\.


--
-- Data for Name: pacientes_examenfisico; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pacientes_examenfisico (id, paciente_id, fecha, apariencia, apariencia_glosa, piel, piel_glosa, cabeza, cabeza_glosa, ojos, ojos_glosa, pecho, pecho_glosa, corazon, corazon_glosa, abdomen, abdomen_glosa, extremidades, extremidades_glosa) FROM stdin;
\.


--
-- Data for Name: pacientes_examenneurologico; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pacientes_examenneurologico (id, paciente_id, fecha, estado_mental, estado_mental_glosa, nervios_craneales, nervios_craneales_glosa, sistema_motor, sistema_motor_glosa, sistema_sensorial, sistema_sensorial_glosa, reflejos, reflejos_glosa, coordinacion, coordinacion_glosa) FROM stdin;
\.


--
-- Data for Name: pacientes_examensignosvitales; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pacientes_examensignosvitales (id, paciente_id, fecha, presion_arterial, pulso, altura, peso) FROM stdin;
\.


--
-- Data for Name: pacientes_familiar; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pacientes_familiar (id, paciente_id, parentesco) FROM stdin;
\.


--
-- Data for Name: pacientes_neuroimagen; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pacientes_neuroimagen (id, paciente_id, fecha, imagen) FROM stdin;
\.


--
-- Data for Name: pacientes_paciente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY pacientes_paciente (id, sexo, nacimiento, raza, raza_otro, test_genetico, tripletes, fecha_consentimiento, fecha_diagnostico, fecha_sintomas, fecha_tratamiento, medicacion, medicacion_glosa, enfermedades_pasadas, enfermedades_pasadas_glosa, cirugias, cirugias_glosa) FROM stdin;
\.


--
-- Data for Name: viales_linea; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY viales_linea (id, nombre, descripcion) FROM stdin;
1	C6 shRNA GLUT1	
2	C6 shRNA GLUT3	
3	Hdh Q111	
4	Hdh Q07	
6	HEK293T	
7	NG108	
5	C6	
\.


--
-- Data for Name: viales_stock; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY viales_stock (id, nombre, descripcion) FROM stdin;
1	Tanque de nitrógeno	
\.


--
-- Data for Name: viales_vial; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY viales_vial (id, ubicacion, fecha, linea_id, stock_id, vigente, observaciones, usuario_id, descongelacion, usuario_descongela_id) FROM stdin;
1	E1	2011-12-29	6	1	S	Probando	5	\N	\N
\.


--
-- Data for Name: vivero_genotipo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY vivero_genotipo (id, genotipo) FROM stdin;
1	homocigoto
2	heterocigoto
\.


--
-- Data for Name: vivero_historico; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY vivero_historico (id, raton_id, instante, estado, evento, usuario_id) FROM stdin;
2	2	2011-12-24 17:35:23.075108-03	V	ingreso	1
3	2	2011-12-24 19:31:00.799656-03	V	reserva	1
4	2	2011-12-25 00:00:02.190923-03	A	reserva	1
5	2	2011-12-26 00:00:01.746017-03	V	fin reserva	1
6	2	2011-12-29 11:20:57.923037-03	V	revisión	1
\.


--
-- Data for Name: vivero_imagenraton; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY vivero_imagenraton (id, raton_id, imagen, fecha, descripcion) FROM stdin;
1	2	ratones/imagenes/2/Koala.jpg	2011-12-24	
\.


--
-- Data for Name: vivero_linea; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY vivero_linea (id, linea) FROM stdin;
1	blanco
\.


--
-- Data for Name: vivero_raton; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY vivero_raton (id, linea_id, camada, numero, sexo, genotipo_id, regenotipo_id, nacimiento, colonia, estado, muerte, observaciones, padre_id, madre_id) FROM stdin;
2	1	a	1	F	1	1	2011-12-24	a	V	\N		\N	\N
\.


--
-- Data for Name: vivero_reserva; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY vivero_reserva (id, raton_id, usuario_id, tipo, fecha, fecha_termino, creada, observaciones) FROM stdin;
1	2	1	T	2011-12-25	2011-12-26	2011-12-24 19:31:00.792912-03	
\.


--
-- Data for Name: vivero_revision; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY vivero_revision (id, raton_id, fecha, peso, aspecto, aspecto_puntaje, comportamiento, comportamiento_puntaje, signos, signos_puntaje, constantes, constantes_puntaje) FROM stdin;
1	2	2011-12-29	300	asdf	0	asdf	1	asdf	3	asdf	3
\.


--
-- Data for Name: vivero_videoraton; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY vivero_videoraton (id, raton_id, video, fecha, descripcion) FROM stdin;
\.


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_message_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_message
    ADD CONSTRAINT auth_message_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: pacientes_evaluacionfuncional_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pacientes_evaluacionfuncional
    ADD CONSTRAINT pacientes_evaluacionfuncional_pkey PRIMARY KEY (id);


--
-- Name: pacientes_evaluacionmotora_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pacientes_evaluacionmotora
    ADD CONSTRAINT pacientes_evaluacionmotora_pkey PRIMARY KEY (id);


--
-- Name: pacientes_examenfisico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pacientes_examenfisico
    ADD CONSTRAINT pacientes_examenfisico_pkey PRIMARY KEY (id);


--
-- Name: pacientes_examenneurologico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pacientes_examenneurologico
    ADD CONSTRAINT pacientes_examenneurologico_pkey PRIMARY KEY (id);


--
-- Name: pacientes_examensignosvitales_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pacientes_examensignosvitales
    ADD CONSTRAINT pacientes_examensignosvitales_pkey PRIMARY KEY (id);


--
-- Name: pacientes_familiar_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pacientes_familiar
    ADD CONSTRAINT pacientes_familiar_pkey PRIMARY KEY (id);


--
-- Name: pacientes_neuroimagen_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pacientes_neuroimagen
    ADD CONSTRAINT pacientes_neuroimagen_pkey PRIMARY KEY (id);


--
-- Name: pacientes_paciente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pacientes_paciente
    ADD CONSTRAINT pacientes_paciente_pkey PRIMARY KEY (id);


--
-- Name: viales_linea_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY viales_linea
    ADD CONSTRAINT viales_linea_pkey PRIMARY KEY (id);


--
-- Name: viales_stock_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY viales_stock
    ADD CONSTRAINT viales_stock_pkey PRIMARY KEY (id);


--
-- Name: viales_vial_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY viales_vial
    ADD CONSTRAINT viales_vial_pkey PRIMARY KEY (id);


--
-- Name: vivero_genotipo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vivero_genotipo
    ADD CONSTRAINT vivero_genotipo_pkey PRIMARY KEY (id);


--
-- Name: vivero_historico_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vivero_historico
    ADD CONSTRAINT vivero_historico_pkey PRIMARY KEY (id);


--
-- Name: vivero_imagenraton_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vivero_imagenraton
    ADD CONSTRAINT vivero_imagenraton_pkey PRIMARY KEY (id);


--
-- Name: vivero_linea_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vivero_linea
    ADD CONSTRAINT vivero_linea_pkey PRIMARY KEY (id);


--
-- Name: vivero_raton_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vivero_raton
    ADD CONSTRAINT vivero_raton_pkey PRIMARY KEY (id);


--
-- Name: vivero_reserva_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vivero_reserva
    ADD CONSTRAINT vivero_reserva_pkey PRIMARY KEY (id);


--
-- Name: vivero_revision_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vivero_revision
    ADD CONSTRAINT vivero_revision_pkey PRIMARY KEY (id);


--
-- Name: vivero_videoraton_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vivero_videoraton
    ADD CONSTRAINT vivero_videoraton_pkey PRIMARY KEY (id);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_message_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_message_user_id ON auth_message USING btree (user_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: pacientes_evaluacionfuncional_paciente_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pacientes_evaluacionfuncional_paciente_id ON pacientes_evaluacionfuncional USING btree (paciente_id);


--
-- Name: pacientes_evaluacionmotora_paciente_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pacientes_evaluacionmotora_paciente_id ON pacientes_evaluacionmotora USING btree (paciente_id);


--
-- Name: pacientes_examenfisico_paciente_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pacientes_examenfisico_paciente_id ON pacientes_examenfisico USING btree (paciente_id);


--
-- Name: pacientes_examenneurologico_paciente_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pacientes_examenneurologico_paciente_id ON pacientes_examenneurologico USING btree (paciente_id);


--
-- Name: pacientes_examensignosvitales_paciente_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pacientes_examensignosvitales_paciente_id ON pacientes_examensignosvitales USING btree (paciente_id);


--
-- Name: pacientes_familiar_paciente_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pacientes_familiar_paciente_id ON pacientes_familiar USING btree (paciente_id);


--
-- Name: pacientes_neuroimagen_paciente_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX pacientes_neuroimagen_paciente_id ON pacientes_neuroimagen USING btree (paciente_id);


--
-- Name: viales_vial_linea_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX viales_vial_linea_id ON viales_vial USING btree (linea_id);


--
-- Name: viales_vial_stock_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX viales_vial_stock_id ON viales_vial USING btree (stock_id);


--
-- Name: viales_vial_usuario_descongela_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX viales_vial_usuario_descongela_id ON viales_vial USING btree (usuario_descongela_id);


--
-- Name: viales_vial_usuario_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX viales_vial_usuario_id ON viales_vial USING btree (usuario_id);


--
-- Name: vivero_historico_raton_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_historico_raton_id ON vivero_historico USING btree (raton_id);


--
-- Name: vivero_historico_usuario_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_historico_usuario_id ON vivero_historico USING btree (usuario_id);


--
-- Name: vivero_imagenraton_raton_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_imagenraton_raton_id ON vivero_imagenraton USING btree (raton_id);


--
-- Name: vivero_raton_genotipo_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_raton_genotipo_id ON vivero_raton USING btree (genotipo_id);


--
-- Name: vivero_raton_linea_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_raton_linea_id ON vivero_raton USING btree (linea_id);


--
-- Name: vivero_raton_madre_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_raton_madre_id ON vivero_raton USING btree (madre_id);


--
-- Name: vivero_raton_padre_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_raton_padre_id ON vivero_raton USING btree (padre_id);


--
-- Name: vivero_raton_regenotipo_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_raton_regenotipo_id ON vivero_raton USING btree (regenotipo_id);


--
-- Name: vivero_reserva_raton_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_reserva_raton_id ON vivero_reserva USING btree (raton_id);


--
-- Name: vivero_reserva_usuario_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_reserva_usuario_id ON vivero_reserva USING btree (usuario_id);


--
-- Name: vivero_revision_raton_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_revision_raton_id ON vivero_revision USING btree (raton_id);


--
-- Name: vivero_videoraton_raton_id; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX vivero_videoraton_raton_id ON vivero_videoraton USING btree (raton_id);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_message_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_message
    ADD CONSTRAINT auth_message_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_728de91f; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_728de91f FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_3cea63fe; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_3cea63fe FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: madre_id_refs_id_3908ee89; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_raton
    ADD CONSTRAINT madre_id_refs_id_3908ee89 FOREIGN KEY (madre_id) REFERENCES vivero_raton(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pacientes_evaluacionfuncional_paciente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pacientes_evaluacionfuncional
    ADD CONSTRAINT pacientes_evaluacionfuncional_paciente_id_fkey FOREIGN KEY (paciente_id) REFERENCES pacientes_paciente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pacientes_evaluacionmotora_paciente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pacientes_evaluacionmotora
    ADD CONSTRAINT pacientes_evaluacionmotora_paciente_id_fkey FOREIGN KEY (paciente_id) REFERENCES pacientes_paciente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pacientes_examenfisico_paciente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pacientes_examenfisico
    ADD CONSTRAINT pacientes_examenfisico_paciente_id_fkey FOREIGN KEY (paciente_id) REFERENCES pacientes_paciente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pacientes_examenneurologico_paciente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pacientes_examenneurologico
    ADD CONSTRAINT pacientes_examenneurologico_paciente_id_fkey FOREIGN KEY (paciente_id) REFERENCES pacientes_paciente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pacientes_examensignosvitales_paciente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pacientes_examensignosvitales
    ADD CONSTRAINT pacientes_examensignosvitales_paciente_id_fkey FOREIGN KEY (paciente_id) REFERENCES pacientes_paciente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pacientes_familiar_paciente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pacientes_familiar
    ADD CONSTRAINT pacientes_familiar_paciente_id_fkey FOREIGN KEY (paciente_id) REFERENCES pacientes_paciente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: pacientes_neuroimagen_paciente_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY pacientes_neuroimagen
    ADD CONSTRAINT pacientes_neuroimagen_paciente_id_fkey FOREIGN KEY (paciente_id) REFERENCES pacientes_paciente(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: padre_id_refs_id_3908ee89; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_raton
    ADD CONSTRAINT padre_id_refs_id_3908ee89 FOREIGN KEY (padre_id) REFERENCES vivero_raton(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_7ceef80f; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_7ceef80f FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_dfbab7d; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_dfbab7d FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: viales_vial_linea_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY viales_vial
    ADD CONSTRAINT viales_vial_linea_id_fkey FOREIGN KEY (linea_id) REFERENCES viales_linea(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: viales_vial_stock_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY viales_vial
    ADD CONSTRAINT viales_vial_stock_id_fkey FOREIGN KEY (stock_id) REFERENCES viales_stock(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: viales_vial_usuario_descongela_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY viales_vial
    ADD CONSTRAINT viales_vial_usuario_descongela_id_fkey FOREIGN KEY (usuario_descongela_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: viales_vial_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY viales_vial
    ADD CONSTRAINT viales_vial_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vivero_historico_raton_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_historico
    ADD CONSTRAINT vivero_historico_raton_id_fkey FOREIGN KEY (raton_id) REFERENCES vivero_raton(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vivero_historico_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_historico
    ADD CONSTRAINT vivero_historico_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vivero_imagenraton_raton_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_imagenraton
    ADD CONSTRAINT vivero_imagenraton_raton_id_fkey FOREIGN KEY (raton_id) REFERENCES vivero_raton(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vivero_raton_genotipo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_raton
    ADD CONSTRAINT vivero_raton_genotipo_id_fkey FOREIGN KEY (genotipo_id) REFERENCES vivero_genotipo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vivero_raton_linea_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_raton
    ADD CONSTRAINT vivero_raton_linea_id_fkey FOREIGN KEY (linea_id) REFERENCES vivero_linea(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vivero_raton_regenotipo_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_raton
    ADD CONSTRAINT vivero_raton_regenotipo_id_fkey FOREIGN KEY (regenotipo_id) REFERENCES vivero_genotipo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vivero_reserva_raton_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_reserva
    ADD CONSTRAINT vivero_reserva_raton_id_fkey FOREIGN KEY (raton_id) REFERENCES vivero_raton(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vivero_reserva_usuario_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_reserva
    ADD CONSTRAINT vivero_reserva_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vivero_revision_raton_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_revision
    ADD CONSTRAINT vivero_revision_raton_id_fkey FOREIGN KEY (raton_id) REFERENCES vivero_raton(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: vivero_videoraton_raton_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY vivero_videoraton
    ADD CONSTRAINT vivero_videoraton_raton_id_fkey FOREIGN KEY (raton_id) REFERENCES vivero_raton(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

