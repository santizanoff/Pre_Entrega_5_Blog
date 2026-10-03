# main.py
from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post

if __name__ == "__main__":
    print("Bienvenido al Gestor de Blog Modular")
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == 1:
            listar_posts(posts)
            
        elif opcion == 2:
            termino = input("Ingresa el término a buscar en los títulos: ").strip()
            if termino:
                buscar_por_titulo(posts, termino)
            else:
                print("Error: El término de búsqueda no puede estar vacío.")
                
        elif opcion == 3:
            tag = input("Ingresa el tag para filtrar: ").strip()
            if tag:
                filtrar_por_tag(posts, tag)
            else:
                print("Error: El tag no puede estar vacío.")
                
        elif opcion == 4:
            print("\n--- VALIDACIÓN DE POSTS ---")
            for post in posts:
                id_post = post.get("id", "Desconocido")
                es_valido, mensaje = validar_post(post)
                if es_valido:
                    print(f"Post {id_post}: válido")
                else:
                    print(f"Post {id_post}: error - {mensaje}")
                    
        elif opcion == 5:
            print("Saliendo del sistema... ¡Hasta luego!")
            break
            
        elif opcion == -1:
            print("Error: Por favor ingresa un NÚMERO válido.")
        else:
            print("Error: Opción inexistente. Elige un número del 1 al 5.")