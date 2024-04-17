import ply.lex as lex

resultado_lexema = []

# Palabras reservadas
reserved = {
    'USING': 'USING',
    'NAMESPACE': 'NAMESPACE',
    'MAIN': 'MAIN',
    'ARGS': 'ARGS',
    'SYSTEM': 'SYSTEM',
    'CONSOLE': 'CONSOLE',
    'CLASS': 'CLASS',
    'STATIC': 'STATIC',
    'VOID': 'VOID',
    'STRING': 'STRING',
    'WRITELINE': 'WRITELINE',
}

tokens = [
    #Logicos
    'MENORQUE',
    'MAYORQUE',
    'MENORIGUAL',
    'MAYORIGUAL',
    'DISTINTO',


    'IDENTIFICADOR',
    'ENTERO',
    'CADENA',
    'ASIGNAR',
    
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'MODULO',
    
    'PLUSPLUS',
    'MINUSMINUS',
    

    # Simbolos
    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    'NUMERAL',
    
    # Otros
    'PUNTO',
    'PUNTOCOMA',
    'COMA',
    'COMILLA_SIMPLE',
    'COMDOB',
    'MAYORDER', 
    'MAYORIZQ', 
    'COMMENT',
]+ list(reserved.values())


# Expresiones regulares para tokens simples
t_CADENA = r'\"([^\\\n]|(\\.))*?\"'


t_ASIGNAR = r'='

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'

t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'\-\-'

t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_MENORIGUAL = r'<='
t_MAYORIGUAL = r'>='
t_DISTINTO = r'!='

t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_NUMERAL = r'\#'

t_PUNTO = r'\.'
t_PUNTOCOMA = r';'
t_COMA = r','
t_COMILLA_SIMPLE = r'\''

t_MAYORDER = r'>>'
t_MAYORIZQ = r'<<'


# Regla para identificadores
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z]*'
    if t.value.upper() in reserved: 
        t.type = reserved[t.value.upper()]  
    else:
        t.type = 'IDENTIFICADOR'  
    return t

# Regla para números
def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regla para comentarios
def t_COMMENT(t):
    r'//.*'
    pass

# Ignorar caracteres como espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print("Carácter no válido '%s' en el token %d" % (t.value[0], t.lexpos))
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        resultado_lexema.append(estado)
    return resultado_lexema

# Construir el analizador léxico
lexer = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("Ingrese: ")
        prueba(data)
        print(resultado_lexema)