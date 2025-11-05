import sys
from antlr4 import *
from forLexer import forLexer
from forParser import forParser
from forVisitor import forVisitor 

def main():
    # Código de prueba que causaba errores sintácticos
    codigo_entrada = """
    i = 10;
    x = 10;
    
    // Este bloque causaba error: x = x * 2; y otra_var = j + 1;
    for (j = 0; j < i; j++) {
        x = x * 2; // Multiplicación
        otra_var = j + 1; // Suma
    }
    
    final_x = x; 
    final_j = j;
    """
    
    # --- ANÁLISIS SINTÁCTICO Y EJECUCIÓN ---
    
    input_stream = InputStream(codigo_entrada)
    lexer = forLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = forParser(stream)
    
    # Inicia el análisis
    tree = parser.programa()
    
    # Inicia el Visitor (Intérprete)
    interprete = forVisitor()
    interprete.visit(tree)
    
    # --- VERIFICACIÓN DE RESULTADOS ---
    
    print("\n---------------------------------")
    print("✨ Ejecución del Programa Completa ✨")
    print("---------------------------------")
    
    memoria_final = interprete.memoria
    
    print(f"-> Valor final de 'x' (10 * 2^10 = 10240): {memoria_final.get('final_x', 'N/D')}")
    print(f"-> Valor final de 'j' (i=10 veces): {memoria_final.get('final_j', 'N/D')}")
    print(f"-> Valor final de 'otra_var': {memoria_final.get('otra_var', 'N/D')}")
    
    print("\nMEMORIA COMPLETA:", memoria_final)
    print("---------------------------------")

if __name__ == '__main__':
    main()