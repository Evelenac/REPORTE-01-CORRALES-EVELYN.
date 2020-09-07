# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 10:52:39 2020

@author: evely
"""
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

print("Welcome to LifeStore Inventory")


print("Account Login")

users = ["user1", "user2", "user3"] # usuarios permitidos 
users_passwords = ["111","222","333"]
admins = ["admin1", "admin2", "admin3"]# administradores permitidos
admins_passwords = ["a111","a222","a333"]


#Prueba de acceso
access = True
admin = False
user= False
while access:
    enter_username = input("Enter username: ")
    enter_password = input("Enter password: ")

    if enter_username in users:
        if enter_username == users[0] and enter_password == users_passwords[0]:
            access = False
            user = True
            print("LOGIN as user1")
        elif enter_username == users[1] and enter_password == users_passwords[1]:
            access = False
            user = True
            print("LOGIN as user2")
        elif enter_username == users[2] and enter_password == users_passwords[2]:
            access = False
            user = True
            print("LOGIN as user3")
        else: 
            print("Invalid username or password. Please try again.")
        
    elif enter_username in admins:
        if enter_username == admins[0] and enter_password == admins_passwords[0]:
            access = False
            admin = True
            print("LOGIN as admin1")
        elif enter_username == admins[1] and enter_password == admins_passwords[1]:
            access = False
            admin = True
            print("LOGIN as admin2")
        elif enter_username == admins[2] and enter_password == admins_passwords[2]:
            access = False
            admin = True
            print("LOGIN as admin3") 
        else: 
            print("Invalid username or password. Please try again.")
    else:
        print("Sorry, something went worng....")
        print("That account does not exist. Please enter a different account.\n(TIP: user or admin)")
        access = True
          
continuar = input("Next:(yes/no)")
while continuar == "yes":
    option_1 = False
    option_2 = False
    option_3 = False
    option_4 = False
    option_5 = False
    option_6 = False
    option_7 = False
    option_8 = False
    option_9 = False
    
    if admin == True or user == True:        
        print("You access as administrator\n Options as admin:\n 1)TOP  50 searches\n 2)BOTTOM searches\n" 
              " 3)PRODUCTS searches by category \n 4)TOTAL SEARCHES AND SALES by category \n 5)PRODUCTS sales by category\n"
              " 6)TOP 50 sales\n 7)TOP 20 and BOTTOM 20 Reviews\n 8)ANUAL REVENUE-SALES and AVERAGE REVENUE BY MONTH \n"
              " 9)TOTAL SALES by MONTH and MONTHS TOP sales")
        select_option =input("Select the option: ")
        if select_option == "1":
            print("Selected: ---TOP 50 SEARCHES---")
            option_1 = True 
        elif select_option == "2":
            print("Selected: Bottom searches")
            option_2 = True
        elif select_option == "3":
            print("Selected: Products searches by category")
            option_3 = True
        elif select_option == "4":
             print("Selected:--- TOTAL SEARCHES AND SALES by category---")
             option_4 = True
        elif select_option == "5":
             print("Selected: Products sales by category")
             option_5 = True
        elif select_option == "6":
             print("Selected: --TOP 50 SALES--")
             option_6 = True
        elif select_option == "7":
             print("Selected:-- TOP 20 and BOTTOM 20 REVIEWS--")
             option_7 = True
        elif select_option == "8":
             print("Selected:--ANUAL REVENUE-SALES and AVERAGE REVENUE BY MONTH--")
             option_8 = True 
        elif select_option == "9":
             print("Selected:-- TOTAL SALES by MONTH and MONTHS TOP SALES-- ")
             option_9 = True
             
        else:
            print(("Sorry, something went worng...."))
            print(("Try with 1 ,2, 3, 4 up to 9"))
    

#print(option_1)
#print(option_2)

#--------Separar las sublistas de las listas principales-------------

    frequency_lst = list()
    for searches in lifestore_searches:
        frequency_lst.append(searches[1])
    
    
    name_lst = list()
    prices = list()  
    id_lst = list()  
    category_lst = list()
    frequency_category = list()
    for products in lifestore_products:  
        name_lst.append(products[1])
        id_lst.append(products[0])
        frequency_category.append(products[3])
        prices.append(products[2])
        
        if products[3] not in category_lst:
            category_lst.append(products[3])
    
    dates = list() #todas las fechas
    dates2= list() #fechas unicas
    frequency_sales = list()
    scores_frequency = list()
    refund = list()
    for sales in lifestore_sales:
        frequency_sales.append(sales[1]) #cuantas veces se vende un producto
        scores_frequency.append(sales[2])
        refund.append(sales[4])
        dates.append(sales[3]) #todos los dias del año que hubo venta
        if sales[3] not in dates2:
            dates2.append(sales[3])
     
        
    #----------------------SECCION BUSQUEDAS--------------------------------
    #1a)PRODUCTOS CON MAYORES BUSQUEDAS 
    #-----------Contar las veces que se busca el id producto --------------
    final_lst = list()
    reporte_category = list()
    for ids in range(len(id_lst)):#lista con los ids que tuvieron busqueda
        count = 0
        for freq in range(len(frequency_lst)): # listas de busquedas
            if(frequency_lst[freq] == id_lst[ids]): # cuantas veces se repite la busqueda por id
                count = count + 1
        report_search = [count,id_lst[ids],name_lst[ids]]
        report_category_search = [count,name_lst[ids],frequency_category[ids]]
        final_lst.append(report_search)
        reporte_category.append(report_category_search) #reporte con el total de busquedas
    #print(reporte_category)
    final_lst.sort(reverse=True)#ordenar de mayor a menor las busquedas   
    final_lst2 = final_lst[0:50]# rango de mayores busquedas
    final_lst3 = final_lst2#lista con resultados finales de mayores busquedas
    reporte_category.sort()
    #print(final_lst)
    
    
    #RESULTADOS DE LAS MAYORES BUSQUEDAS--VALIDADO
    #Resultados 1a):
    if option_1 == 1:
        print("Loading...")
        print("Results:")
        print("PRODUCTS SEARCHES TOP 50")
        for searches_top in final_lst2:
            print("|Searches:",searches_top[0],"|"" \n| Product:",searches_top[2], "|id: ",searches_top[1],"|")
            print("____________________________________________________________________________________")
        print("Completed")
        
        continuar = input("new selection (yes/no): ")
        if continuar == "yes":
            print("loading...")
        elif continuar == "no":
            print("logggin out..")
               
        else: print("type: yes or no")
        continue
         
    if option_2 == 1:      
        print("PRODUCTS SEARCHES BOTTOM 50")
        print("Loading...")
        print("Results:")
        for searches_bottom in final_lst[-51:-1]:
            print("|Searches: ",searches_bottom[0],"|\n""| Product:",searches_bottom[2], "|id: ",searches_bottom[1],"|")
            print("_________________________________________________________________________")
        print("Completed")
        
        continuar = input("new selection (yes/no): ")
        if continuar == "yes":
            print("loading...")            
        elif continuar == "no":
            print("logggin out..")
               
        else: print("type: yes or no")
        continue


#2a)BUSQUEDAS POR CATEGORIA: 
#--------------..Calcular los productos con menores busquedas------------
# 1)Hacer lista clasificando las categorias

    procesadores_search = list()
    procesadores_search2 = list()
    tarjetas_video_search = list()
    tarjetas_video_search2 = list()
    tarjetas_madre_search = list()
    tarjetas_madre_search2 = list()
    discos_duros_search = list()
    discos_duros_search2 = list()
    memorias_usb_search = list()
    memorias_usb_search2 = list()
    pantallas_search = list()
    pantallas_search2 = list()
    bocinas_search = list()
    bocinas_search2 = list()
    audifonos_search = list()
    audifonos_search2 = list()
    
    for category_search in reporte_category:
        if category_search[2] == "procesadores":
            procesadores_search.append(category_search[0]) #Lista de solo cantidad de busquedas x categoria
            procesadores_search2.append(category_search)#Lista de cantidad de busquedas,producto x categoria
        elif category_search[2] == "tarjetas de video":
            tarjetas_video_search.append(category_search[0])
            tarjetas_video_search2.append(category_search)
        elif category_search[2] == "tarjetas madre":
            tarjetas_madre_search.append(category_search[0])
            tarjetas_madre_search2.append(category_search)
        elif category_search[2] == "discos duros":
            discos_duros_search.append(category_search[0])
            discos_duros_search2.append(category_search)
        elif category_search[2] == "memoria usb":
            memorias_usb_search.append(category_search[0])
            memorias_usb_search2.append(category_search)
        elif category_search[2] == "pantallas":
            pantallas_search.append(category_search[0])
            pantallas_search2.append(category_search)
        elif category_search[2] == "bocinas":
            bocinas_search.append(category_search[0])
            bocinas_search2.append(category_search)
        elif category_search[2] == "audifonos":
            audifonos_search.append(category_search[0])
            audifonos_search2.append(category_search)
    
    procesadores_search2.sort()
    tarjetas_video_search2.sort()
    tarjetas_madre_search2.sort()
    discos_duros_search2.sort()
    memorias_usb_search2.sort()
    pantallas_search2.sort()
    bocinas_search2.sort()
    audifonos_search2.sort()

#RESULTADOS DE BUSQUEDAS MENOS A MAS POR PRODUCTO EN CADA CATEGORIA
#Resultados 2a)
    if option_3 == 1: 
        print('SEARCHES IN: "PROCESADORES"\n'
              'Loading...\n'
              'Results:\n')
        for column in procesadores_search2:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SEARCHES: ",column[0],"|\n")
            print("_____________________________________________________________________________")
        print("Completed")
    
        print('SEARCHES IN: "TARJETAS DE VIDEO"\n'
              'Loading...\n'
              'Results:\n')
        for column in tarjetas_video_search2:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SEARCHES: ",column[0],"|\n")
            print("_____________________________________________________________________________")
        print("Completed")
        
        print('SEARCHES IN: "TARJETAS MADRE"\n'
              'Loading...\n'
              'Results:\n')
        for column in tarjetas_madre_search2:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SEARCHES: ",column[0],"|\n")
            print("_____________________________________________________________________________")
        print("Completed")
                 
        print('SEARCHES IN: "DISCOS DUROS"\n'
              'Loading...\n'
              'Results:\n')
        for column in discos_duros_search2:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SEARCHES: ",column[0],"|\n")
            print("_____________________________________________________________________________")
        print("Completed")
    
        print('SEARCHES IN: "MEMORIAS USB"\n'
              'Loading...\n'
              'Results:\n')
        for column in memorias_usb_search2:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SEARCHES: ",column[0],"|\n")
            print("_____________________________________________________________________________")
        print("Completed")
        
        print('SEARCHES IN: "PANTALLAS"\n'
              'Loading...\n'
              'Results:\n')
        for column in pantallas_search2:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SEARCHES: ",column[0],"|\n")
            print("_____________________________________________________________________________")
        print("Completed")
        
        print('SEARCHES IN: "BOCINAS"\n'
              'Loading...\n'
              'Results:\n')
        for column in bocinas_search2:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SEARCHES: ",column[0],"|\n")
            print("_____________________________________________________________________________")   
        print("Completed")               
    
        print('SEARCHES IN: "AUDIFONOS"\n'
              'Loading...\n'
              'Results:\n')
        for column in audifonos_search2:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SEARCHES: ",column[0],"|\n")
            print("_____________________________________________________________________________")
        print("Completed")
        
        continuar = input("new selection (yes/no): ")
        if continuar == "yes":
            print("loading...")
        elif continuar == "no":
            print("logggin out..")
               
        else: print("type: yes or no")
        continue

# 1c) BUSQUEDAS TOTALES DE LAS CATEGORIAS
# 2. -----------Calcular busquedas totales en cada categoria--------------
    total_procesadores = 0
    for procesador_search in procesadores_search:
        total_procesadores = total_procesadores + procesador_search
    
    total_tarjetasv = 0
    for tarjetasv_search in tarjetas_video_search:
        total_tarjetasv = total_tarjetasv + tarjetasv_search
    
    total_tarjetasm = 0 
    for tarjetasm_search in tarjetas_madre_search:
        total_tarjetasm = total_tarjetasm + tarjetasm_search 
    
    total_discod = 0 
    for dscosd_search in discos_duros_search:
        total_discod = total_discod + dscosd_search 
    
    total_memorias = 0
    for memorias_search in memorias_usb_search:
        total_memorias = total_memorias + memorias_search
    #print(total_memorias)
    
    total_pantallas = 0
    for pantalla_search in pantallas_search:
        total_pantallas = total_pantallas + pantalla_search
    #print(total_pantallas)
    
    total_bocinas = 0
    for bocina_search in bocinas_search:
        total_bocinas = total_bocinas + bocina_search
    #print(total_bocinas)
    
    total_audifonos = 0
    for audifono_search in audifonos_search:
        total_audifonos = total_audifonos + audifono_search
    #print(total_audifonos)
    
    #3. Concatenar una lista: usando las ventas totales por
    #categoria y el nombre de la categoria
    
    #Crear lista de las busquedas totales por categoria
    categories = ([total_procesadores , total_tarjetasv , total_tarjetasm
                  , total_discod , total_memorias , total_pantallas
                  , total_bocinas  , total_audifonos])
    
    #Lista final de categoria con su respetivas busquedas totales
    final_category = list()
    for i in range(len(categories)):
        total_category = [categories[i],category_lst[i]]
        final_category.append(total_category)
        #print(total_category)
        
    final_category.sort()
#print(final_category)
#RESULTADOS DE LAS BUSQUEDAS TOTALES POR CATEGORIA

#RESULTADOS DE BUSQUEDAS TOTALES DE CADA CATEGORIA -validado
#Resultados 1c):
    if option_4 == 1:
        print("Loading...")
        print("Results:") 
        print("TOTAL SEARCHES by CATEGORY:\n")
        for scategory in final_category:
            print("|Searches:",scategory[0],  " Category:",scategory[1])
            print("|---------------------------------------------------|")
        print("Completed")

  
#<-------------------TERMINA SECCION 1 BUSQUEDAS-------------------------->

#---------------------------SECION2 VENTAS-------------------------------->
# Contar las ventas de cada producto y sacar las mayores
# 2b) MAYORES VENTAS POR PRODUCTO
    sales_lst = list()
    sales_lst2 = list()
    sales_lst3 = list() # para sacar ventas por mes
    for ids in range(len(id_lst)):
        count = 0
        for freq in range(len(frequency_sales)):
            if (frequency_sales[freq] == id_lst[ids]):
                count = count + 1
        #print(count)
        report_sales = [count,id_lst[ids],name_lst[ids]]
        report_sales2 =[count,name_lst[ids],frequency_category[ids]]
        sales_lst.append(report_sales)
        sales_lst2.append(report_sales2)
              
    #print(sales_lst2)
    sales_lst.sort(reverse=True)#ordenado de mayor a menor
    sales_max = sales_lst[0:50] #mayores 50 ventas por producto
    sales_lst2.sort()
    sales_min = sales_lst2[0:50]#menores 50 ventas por producto
    #print(sales_max)
    #RESULTADOS DE LOS PRODUCTOS CON MAYORES VENTAS
    
    
    
    #Resultados 1b): validaddo
    
    if option_6 == 1:
        print("Loading...")
        print("Results:")    
        print(" PRODUCTS SALES TOP 50:\n")
        for sales_top in sales_max:
            print("|Total SALES: ",sales_top[0],"|id: ",sales_top[1],"| Product:",sales_top[2],"|")
            print("-----------------------------------------------------------------------------\n")
        print("Completed")
        
        continuar = input("new selection (yes/no): ")
        if continuar == "yes":
            print("loading...")
        elif continuar == "no":
            print("logggin out..")
               
        else: print("type: yes or no")
        continue
    
    procesadores_sales= list() 
    procesadores_sales2= list() 
    tarjetas_video_sales = list()
    tarjetas_video_sales2 = list()
    tarjetas_madre_sales = list()
    tarjetas_madre_sales2 = list()
    discos_duros_sales = list()
    discos_duros_sales2 = list()
    memorias_usb_sales = list()
    memorias_usb_sales2 = list()
    pantallas_sales = list()
    pantallas_sales2 = list()
    bocinas_sales = list()
    bocinas_sales2 = list()
    audifonos_sales = list()
    audifonos_sales2 = list()

#FALTA SACAR VENTAS TOTALES EN CADA categoria y hacer lista de las categorias con menos ventas
    for col in sales_lst2:
        if col[2] == "procesadores":
            procesadores_sales.append(col)
            procesadores_sales2.append(col[0])
        elif col[2] == "tarjetas de video":
            tarjetas_video_sales.append(col)
            tarjetas_video_sales2.append(col[0])
        elif col[2] == "tarjetas madre":
            tarjetas_madre_sales.append(col)
            tarjetas_madre_sales2.append(col[0])
        elif col[2] == "discos duros":
            discos_duros_sales.append(col)
            discos_duros_sales2.append(col[0])
        elif col[2] == "memorias usb":
            memorias_usb_sales.append(col)
            memorias_usb_sales2.append(col[0])
        elif col[2] == "pantallas":
            pantallas_sales.append(col)
            pantallas_sales2.append(col[0])
        elif col[2] == "bocinas":
            bocinas_sales.append(col)
            bocinas_sales2.append(col[0])
        elif col[2] == "audifonos":
            audifonos_sales.append(col)
            audifonos_sales2.append(col[0])

#RESULTADOS DE VENTAS MENOS A MAS POR PRODUCTO EN CADA CATEGORIA
#Resultados 2b):
    if option_5 == 1:
        print('SEARCHES IN: "PROCESADORES"\n'
              'Loading...\n'
              'Results:\n')
        for column in procesadores_sales:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SALES: ",column[0],"|\n")
            print("--------------------------------------------------------------------------------------------------\n")
        print("Completed")
    
        print('SEARCHES IN: "TARJETAS DE VIDEO"\n'
              'Loading...\n'
              'Results:\n')
        for column in tarjetas_video_sales:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SALES: ",column[0],"|\n")
            print("--------------------------------------------------------------------------------------------------\n")
        print("Completed")
    
        print('SEARCHES IN: "TARJETAS MADRE"\n'
              'Loading...\n'
              'Results:\n')
        for column in tarjetas_madre_sales:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SALES: ",column[0],"|\n")
            print("--------------------------------------------------------------------------------------------------\n")                
        print("Completed")
        print('SEARCHES IN: "DISCOS DUROS"\n'
              'Loading...\n'
              'Results:\n')
        for column in discos_duros_sales:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SALES: ",column[0],"|\n")
            print("--------------------------------------------------------------------------------------------------\n")
        print("Completed")
        print('SEARCHES IN: "MEMORIAS USB"\n'
              'Loading...\n'
              'Results:\n')
        for column in memorias_usb_sales:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SALES: ",column[0],"|\n")
            print("--------------------------------------------------------------------------------------------------\n")
        print("Completed")    
        print('SEARCHES IN: "PANTALLAS"\n'
              'Loading...\n'
              'Results:\n')
        for column in pantallas_sales:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SALES: ",column[0],"|\n")
            print("--------------------------------------------------------------------------------------------------\n")
        print("Completed")
        print('SEARCHES IN: "BOCINAS"\n'
              'Loading...\n'
              'Results:\n')
        for column in bocinas_sales:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SALES: ",column[0],"|\n")
            print("--------------------------------------------------------------------------------------------------\n")  
        print("Completed")                
        print('SEARCHES IN: "AUDIFONOS"\n'
              'Loading...\n'
              'Results:\n')
        for column in audifonos_sales:
            print("|Category: ",column[2],"| Product:",column[1], "|Total SALES: ",column[0],"|\n")
            print("--------------------------------------------------------------------------------------------------\n")
        print("Completed")
        
        continuar = input("new selection (yes/no): ")
        if continuar == "yes":
            print("loading...")
        elif continuar == "no":
            print("logggin out..")
               
        else: print("type: yes or no")
        continue

# 1c) VENTAS TOTALES DE LAS CATEGORIAS
# 2. Calcular ventas totales en cada categoria
    ventas_procesadores = 0
    for procesador_sales in procesadores_sales2:
        ventas_procesadores = ventas_procesadores + procesador_sales
    
    ventas_tarjetasv = 0
    for tarjetasv_sales in tarjetas_video_sales2:
        ventas_tarjetasv = ventas_tarjetasv + tarjetasv_sales
    
    ventas_tarjetasm = 0 
    for tarjetasm_sales in tarjetas_madre_sales2:
        ventas_tarjetasm = ventas_tarjetasm + tarjetasm_sales 
    
    ventas_discod = 0 
    for dscosd_sales in discos_duros_sales2:
        ventas_discod = ventas_discod + dscosd_sales 
    
    ventas_memorias = 0
    for memorias_sales in memorias_usb_sales2:
        ventas_memorias = ventas_memorias + memorias_sales
    #print(total_memorias)
    
    ventas_pantallas = 0
    for pantalla_sales in pantallas_sales2:
        ventas_pantallas = ventas_pantallas + pantalla_sales
    #print(total_pantallas)
    
    ventas_bocinas = 0
    for bocina_sales in bocinas_sales2:
        ventas_bocinas = ventas_bocinas + bocina_sales
    #print(total_bocinas)
    
    ventas_audifonos = 0
    for audifono_sales in audifonos_sales2:
        ventas_audifonos = ventas_audifonos + audifono_sales
    #print(total_audifonos)
    
#3. Concatenar una lista: usando las ventas totales por
#categoria y el nombre de la categoria
    
#Crear lista de las busquedas totales por categoria
    categories_ventas = ([ventas_procesadores , ventas_tarjetasv , ventas_tarjetasm
                  ,ventas_discod , ventas_memorias , ventas_pantallas
                  , ventas_bocinas  , ventas_audifonos])

#Lista final de categoria con su respetivas busquedas totales
    final_ventas = list()
    for i in range(len(categories_ventas)):
        total_ventas = [categories_ventas[i],category_lst[i]]
        final_ventas.append(total_ventas)
        #print(total_ventas)
    
#RESULTADOS DE VENTAS TOTALES POR CATEGORIA
#Resultados 2c):

#print(final_ventas)
    final_ventas.sort()
#RESULTADOS DE VENTAS TOTALES DE CADA CATEGORIA -validado
    if option_4 == 1:
        print("Loading...")
        print("Results:") 
        print("TOTAL SALES by CATEGORY:")
        for sales_cat in final_ventas:
            print("|SALES:",sales_cat[0],  " Category:",sales_cat[1])
            print("|---------------------------------------------------|")
        print("Completed")
        
        continuar = input("new selection (yes/no): ")
        if continuar == "yes":
            print("loading...")
        elif continuar == "no":
            print("logggin out..")
               
        else: print("type: yes or no")
        continue        

#<-----------------------TERMINA SECCION 2 VENTAS---------------------------->

#---------------------------SECION 3 RESEÑAS--------------------------------->
# Calcular -->
# 1)Hacer lista clasificando las

    name_reseñas = list()
    for ids_reseñas in range(len(id_lst)):
        for tscores in range(len(frequency_sales)):
            if id_lst[ids_reseñas] == frequency_sales[tscores]:
                name_reseñas.append(name_lst[ids_reseñas])
                
    reseñas = list()
    for i in range(len(scores_frequency)):
        total_scores = [name_reseñas[i],scores_frequency[i], refund[i]]
        reseñas.append(total_scores)
    #print(reseñas)
    
    reporte_reseña = list()
    for ids in range(len(id_lst)):#lista con los ids que tuvieron busqueda
        count = 0
        sumas_score = 0
        for freqq in range(len(frequency_sales)): # listas de busquedas
            if(frequency_sales[freqq] == id_lst[ids]): # cuantas veces se repite la busqueda por id
                count = count + 1
                sumas_score = sumas_score + scores_frequency[freqq]
                if sumas_score != 0:
                    promedio = sumas_score/count
                else:
                    promedio = sumas_score
                #print(sumas_score)
            elif refund[freqq] == 0:
                refund_status = "No refund"
                
            else: 
                refund_status ="With refund"
        report_scores = [promedio, name_lst[ids], refund_status]
        reporte_reseña.append(report_scores)
    #print(reporte_reseña)
    reporte_reseña.sort()
    reporte_reseña2 = sorted(reporte_reseña, reverse = True)


#RESULTADOS DE MEJORES Y PEORES RESEÑAS -validado
    if option_7 == 1:
        print("Loading...")
        print("Results:") 
        print("WORST 20 REVIEWS:")
        for reviews in reporte_reseña[0:20]:
            print("|REVIEWS AVERAGE:",reviews[0]," Status Refund:",reviews[2],  " Product:",reviews[1],"|")
            print("|------------------------------------------------------------------------------------|")
        print("Completed")
    
        print("Loading...")
        print("Results:") 
        print("\n" "BETTER 20 REVIEWS:")
        for reviews in reporte_reseña2[0:20]:
            print("|REVIEWS AVERAGE:",reviews[0]," Status Refund:",reviews[2],  " Product:",reviews[1],"|")
            print("|------------------------------------------------------------------------------------|")
        print("Completed")
        
        continuar = input("new selection (yes/no): ")
        if continuar == "yes":
            print("loading...")
        elif continuar == "no":
            print("logggin out..")
               
        else: print("type: yes or no")
        continue


#-------------------------------SECCION 4 finales ----------------------------------->

#Calculo de ventas anuales--------------------------------------- SI
    reporte_score = list()
    for ids in range(len(id_lst)):
        count = 0
        for id_sale in range(len(frequency_sales)):
            if (frequency_sales[id_sale] == id_lst[ids]):
                count = count + 1
        reporte_score.append(count)  
    #print(reporte_score)
        
    ingresos_anuales = list()
    ventas_anuales = list()
    total_ingreso = 0
    total_ventas = 0
    for price in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_anuales.append(prices[price] * reporte_score[price])#precio del producto por el numero de ventas x producto
    
    for ingreso in ingresos_anuales:
        total_ingreso = total_ingreso + ingreso   
    #print(total_ingreso)    
    
    for ventas in reporte_score:
        total_ventas = total_ventas + ventas 
        
        
    if option_8 == 1:
    
        print("\n""TOTAL ANUAL REVENUE AND  SALES ")
        print("--------------------------------------------------------------------------------------------------\n")
        print("| REVENUE : $",total_ingreso, "|SALES: ",total_ventas,"|\n")
        print("--------------------------------------------------------------------------------------------------\n")

#Organizar en meses las ventas y sacar el promedio de cada mes

    new_dates = list()# cambiar posicion de mes de la lista principal de dates
    new_dates2 = list()
    for date in dates:
        dia = date[0:3]
        mes = date[3:6]
        año = date[6:]
        new_date = mes #+ dia + año
        new_dates.append(new_date)
        
        #new_dates2.append(new_date)
    dates_double = list()
    dates_double2 = list()
    for date2 in dates2: #cambiar posicion de mes de la lista secundaria de dates
        dia = date2[0:3]
        mes = date2[3:6]
        año = date2[6:]
        date_double = mes #+ dia + año    
        dates_double.append(date_double)
        #dates_double2.append(date_double2)
#Lista de meses del 1 al 12
    meses = ['01/','02/','03/','04/','05/','06/','07/','08/','09/','10/','11/','12/']
    
    #print(dates_double2)
    #Hacer la comparativa de fechas para calcular las ventas por mes   
    reporte_mensual = list()
    count_lst = list()
    reporte_mensual2 = list()
    for mes in range(len(meses)):
        count = 0
        for date_new in range(len(new_dates)):
            if (new_dates[date_new] == meses[mes]):
                count = count + 1
    
        report_mes = [meses[mes],count]
        report_mes2 = [count,meses[mes]]
        reporte_mensual2.append(report_mes2)
        reporte_mensual.append(report_mes)
        
    reporte_mensual.sort()
    reporte_mensual2.sort(reverse=True)
    
    #print(reporte_mensual2)
    if option_9 == 1:
        
        print("MONTH SALES")
        print("Loading...")
        print("Results:")
    
        print("|-------------------------------|")
        print("| TOTAL SALES JANUARY: ",reporte_mensual[0][1],"      |")
        print("|-------------------------------|")
        print("| TOTAL SALES FEBRUARY: ",reporte_mensual[1][1],"    |")
        print("|-------------------------------|")
        print("| TOTAL SALES MARCH: ",reporte_mensual[2][1],"      |")
        print("|-------------------------------|")
        print("| TOTAL SALES APRIL: ",reporte_mensual[3][1],"      |")
        print("|-------------------------------|")
        print("| TOTAL SALES MAY: ",reporte_mensual[4][1],"       |")
        print("|-------------------------------|")
        print("| TOTAL SALES JUNE: ",reporte_mensual[5][1],"      |")
        print("|-------------------------------|")
        print("| TOTAL SALES JULY: ",reporte_mensual[6][1],"      |")
        print("|-------------------------------|")
        print("| TOTAL SALES AUGUST: ",reporte_mensual[7][1],"      |")
        print("|-------------------------------|")
        print("| TOTAL SALES SEPTEMBER: ",reporte_mensual[8][1],"  |")
        print("|-------------------------------|")
        print("| TOTAL SALES OCTUBER ",reporte_mensual[9][1],"     |")
        print("|-------------------------------|")
        print("| TOTAL SALES NOVEMBER: ",reporte_mensual[10][1],"   |")
        print("|-------------------------------|")
        print("| TOTAL SALES DECEMBER: ",reporte_mensual[11][1],"   |")
        print("|-------------------------------|")
      
    
    
        print("Loading...")
        print("Results:")
        print("TOP SALES by MONTH:")
    
        for ventas2 in reporte_mensual2[0:7]: 
            print("|------------------------------|")
            print("|MES:",ventas2[1],"|Total de ventas:",ventas2[0],)
            print("|------------------------------|")
        print("Completed")
        
        continuar = input("new selection (yes/no): ")
        if continuar == "yes":
            print("loading...")
        elif continuar == "no":
            print("logggin out..")
               
        else: print("type: yes or no")
        continue
#------------Calcular cuanto se vende por mes------------------------------
    revenue = list()
    
    for date_new in range(len(new_dates)):
        count = 0 
        for mes in range(len(meses)):
            if (new_dates[date_new] == meses[mes]):
                count = count + 1
        ganancias = [new_dates[date_new] , frequency_sales[date_new]]
        revenue.append(ganancias) 
    #print(revenue)
    
    enero = list()
    febrero = list()
    marzo = list()
    abril = list()
    mayo = list()
    junio = list()
    julio = list()
    agosto = list()
    septiembre = list()
    octubre = list()
    noviembre = list()
    diciembre = list()
    
    for mes_mes in revenue:
        if mes_mes[0] == meses[0]:
            enero.append(mes_mes)           
        elif mes_mes[0] == meses[1]:
            febrero.append(mes_mes)
        elif mes_mes[0] == meses[2]:
            marzo.append(mes_mes)
        elif mes_mes[0] == meses[3]:
            abril.append(mes_mes)
        elif mes_mes[0] == meses[4]:
            mayo.append(mes_mes)
        elif mes_mes[0] == meses[5]:
            junio.append(mes_mes)
        elif mes_mes[0] == meses[6]:
            julio.append(mes_mes)
        elif mes_mes[0] == meses[7]:
            agosto.append(mes_mes)
        elif mes_mes[0] == meses[8]:
            septiembre.append(mes_mes)
        elif mes_mes[0] == meses[9]:
            octubre.append(mes_mes)
        elif mes_mes[0] == meses[10]:
            noviembre.append(mes_mes)
        elif mes_mes[0] == meses[11]:
            diciembre.append(mes_mes)
        else:
            "no existe"
    #print(marzo)    
    
    #ENERO--->   
    #Tomo los ids de las ventas de enero para compararlos con los ids y su precio
    ids_enero = list()
    for veces in enero:
        ids_enero.append(veces[1])
    #print(ids_enero)
    
    # Creo un reporte que me dice que ids si tuvieron ventas en enero
    reporte_enero = list()
    for ids in range(len(id_lst)):
        count = 0
        for id_enero in range(len(ids_enero)):
            if (ids_enero[id_enero] == id_lst[ids]):
                count = count + 1
        
        reporte_enero.append(count) 
    #print(reporte_enero)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_enero = list()
    for price_enero in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_enero.append(prices[price_enero] * reporte_enero[price_enero])#precio del producto por el numero de ventas x producto
    #print(ingresos_enero)
    
    #Calculo de las ventas totales de enero de los ids
    total_enero = 0
    for ingreso_enero in ingresos_enero:
        total_enero = total_enero + ingreso_enero
    #print(total_enero)
    
    #FEBRERO--->  
    #Tomo los ids de las ventas de febrero para compararlos con los ids y su precio
    ids_febrero = list()
    for veces_febrero in febrero:
        ids_febrero.append(veces_febrero[1])
    #print(ids_febrero)
    
    # Creo un reporte que me dice que ids si tuvieron ventas en febrero
    reporte_febrero = list()
    for ids in range(len(id_lst)):
        count = 0
        for id_febrero in range(len(ids_febrero)):
            if (ids_febrero[id_febrero] == id_lst[ids]):
                count = count + 1
        
        reporte_febrero.append(count) 
    #print(reporte_febrero)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_febrero = list()
    for price_febrero in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_febrero.append(prices[price_febrero] * reporte_febrero[price_febrero])#precio del producto por el numero de ventas x producto
    #print(ingresos_febrero)
    
    #Calculo de las ventas totales de enero de los ids
    total_febrero = 0
    for ingreso_febrero in ingresos_febrero:
        total_febrero = total_febrero + ingreso_febrero
     
    #MARZO--->  
    #Tomo los ids de las ventas de marzo para compararlos con los ids y su precio
    ids_marzo = list()
    for veces_marzo in marzo:
        ids_marzo.append(veces_marzo[1])
    #print(ids_marzo)
    
    # Creo un reporte que me dice que ids si tuvieron ventas en marzo
    reporte_marzo = list()
    for ids in range(len(id_lst)):
        count = 0
        for id_marzo in range(len(ids_marzo)):
            if (ids_marzo[id_marzo] == id_lst[ids]):
                count = count + 1
        
        reporte_marzo.append(count) 
    #print(reporte_marzo)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_marzo = list()
    for price_marzo in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_marzo.append(prices[price_marzo] * reporte_marzo[price_marzo])#precio del producto por el numero de ventas x producto
    #print(ingresos_marzo)
    
    #Calculo de las ventas totales de marzo de los ids
    total_marzo = 0
    for ingreso_marzo in ingresos_marzo:
        total_marzo = total_marzo + ingreso_marzo
        
    #ABRIL--->  
    #Tomo los ids de las ventas de abril para compararlos con los ids y su precio
    ids_abril = list()
    for veces_abril in abril:
        ids_abril.append(veces_abril[1])
    #print(ids_abril)
    
    # Creo un reporte que me dice que ids si tuvieron ventas en abril
    reporte_abril = list()
    for ids in range(len(id_lst)):
        count = 0
        for id_abril in range(len(ids_abril)):
            if (ids_abril[id_abril] == id_lst[ids]):
                count = count + 1
        
        reporte_abril.append(count) 
    #print(reporte_abril)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_abril = list()
    for price_abril in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_abril.append(prices[price_abril] * reporte_abril[price_abril])#precio del producto por el numero de ventas x producto
    #print(ingresos_abril)
    
    #Calculo de las ventas totales de abril de los ids
    total_abril = 0
    for ingreso_abril in ingresos_abril:
        total_abril = total_abril + ingreso_abril
        
    #MAYO--->  
    #Tomo los ids de las ventas de mayo para compararlos con los ids y su precio
    ids_mayo = list()
    for veces_mayo in mayo:
        ids_mayo.append(veces_mayo[1])
    #print(ids_mayo)
    
    # Creo un reporte que me dice que ids si tuvieron ventas en mayo
    reporte_mayo = list()
    for ids in range(len(id_lst)):
        count = 0
        for id_mayo in range(len(ids_mayo)):
            if (ids_mayo[id_mayo] == id_lst[ids]):
                count = count + 1
        
        reporte_mayo.append(count) 
    #print(reporte_mayo)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_mayo = list()
    for price_mayo in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_mayo.append(prices[price_mayo] * reporte_mayo[price_mayo])#precio del producto por el numero de ventas x producto
    #print(ingresos_mayo)
    
    #Calculo de las ventas totales de mayo de los ids
    total_mayo = 0
    for ingreso_mayo in ingresos_mayo:
        total_mayo= total_mayo + ingreso_mayo
        
    #JUNIO--->  
    #Tomo los ids de las ventas de junio para compararlos con los ids y su precio
    ids_junio = list()
    for veces_junio in junio:
        ids_junio.append(veces_junio[1])
    #print(ids_junio)
    
    # Creo un reporte que me dice que ids si tuvieron ventas en junio
    reporte_junio = list()
    for ids in range(len(id_lst)):
        count = 0
        for id_junio in range(len(ids_junio)):
            if (ids_junio[id_junio] == id_lst[ids]):
                count = count + 1
        
        reporte_junio.append(count) 
    #print(reporte_junio)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_junio = list()
    for price_junio in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_junio.append(prices[price_junio] * reporte_junio[price_junio])#precio del producto por el numero de ventas x producto
    #print(ingresos_marzo)
    
    #Calculo de las ventas totales de marzo de los ids
    total_junio = 0
    for ingreso_junio in ingresos_junio:
        total_junio = total_junio + ingreso_junio
    
    #JULIO--->  
    #Tomo los ids de las ventas de julio para compararlos con los ids y su precio
    ids_julio = list()
    for veces_julio in julio:
        ids_julio.append(veces_julio[1])
    #print(ids_julio)
    
    # Creo un reporte que me dice que ids si tuvieron ventas en julio
    reporte_julio = list()
    for ids in range(len(id_lst)):
        count = 0
        for id_julio in range(len(ids_julio)):
            if (ids_julio[id_julio] == id_lst[ids]):
                count = count + 1
        
        reporte_julio.append(count) 
    #print(reporte_julio)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_julio = list()
    for price_julio in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_julio.append(prices[price_julio] * reporte_julio[price_julio])#precio del producto por el numero de ventas x producto
    #print(ingresos_julio)
    
    #Calculo de las ventas totales del mes de los ids
    total_julio = 0
    for ingreso_julio in ingresos_julio:
        total_julio = total_julio + ingreso_julio
    
    #AGOSTO--->  
    #Tomo los ids de las ventas de agosto para compararlos con los ids y su precio
    ids_agosto = list()
    for veces_agosto in agosto:
        ids_agosto.append(veces_agosto[1])
    #print(ids_agosto)
    
    # Creo un reporte que me dice que ids si tuvieron ventas en agosto
    reporte_agosto = list()
    for ids in range(len(id_lst)):
        count = 0
        for id_agosto in range(len(ids_agosto)):
            if (ids_agosto[id_agosto] == id_lst[ids]):
                count = count + 1
        
        reporte_agosto.append(count) 
    #print(reporte_agosto)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_agosto = list()
    for price_agosto in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_agosto.append(prices[price_agosto] * reporte_agosto[price_agosto])#precio del producto por el numero de ventas x producto
    #print(ingresos_agosto)
    
    #Calculo de las ventas totales de agosto de los ids
    total_agosto = 0
    for ingreso_agosto in ingresos_agosto:
        total_agosto= total_agosto + ingreso_agosto
        
    #SEPTIEMBRE--->  
    #Tomo los ids de las ventas de septiembre para compararlos con los ids y su precio
    ids_septiembre = list()
    for veces_septiembre in septiembre:
        ids_septiembre.append(veces_septiembre[1])
    #print(ids_septiembre)
    
    # Creo un reporte que me dice que ids si tuvieron ventas en septiembre
    reporte_septiembre= list()
    for ids in range(len(id_lst)):
        count = 0
        for id_septiembre in range(len(ids_septiembre)):
            if (ids_septiembre[id_septiembre] == id_lst[ids]):
                count = count + 1
        
        reporte_septiembre.append(count) 
    #print(reporte_septiembre)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_septiembre = list()
    for price_septiembre in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_septiembre.append(prices[price_septiembre] * reporte_septiembre[price_septiembre])#precio del producto por el numero de ventas x producto
    #print(ingresos_septiembre)
    
    #Calculo de las ventas totales de septiembre de los ids
    total_septiembre = 0
    for ingreso_septiembre in ingresos_septiembre:
        total_septiembre = total_septiembre + ingreso_septiembre
    
    #OCTUBRE--->  
    #Tomo los ids de las ventas de octubre para compararlos con los ids y su precio
    ids_octubre = list()
    for veces_octubre in octubre:
        ids_octubre.append(veces_octubre[1])
    #print(ids_octubre)
    
    # Creo un reporte que me dice que ids si tuvieron ventas en octubre
    reporte_octubre= list()
    for ids in range(len(id_lst)):
        count = 0
        for id_octubre in range(len(ids_octubre)):
            if (ids_octubre[id_octubre] == id_lst[ids]):
                count = count + 1
        
        reporte_octubre.append(count) 
    #print(reporte_octubre)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_octubre = list()
    for price_octubre in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_octubre.append(prices[price_octubre] * reporte_octubre[price_octubre])#precio del producto por el numero de ventas x producto
    #print(ingresos_octubre)
    
    #Calculo de las ventas totales de octubre de los ids
    total_octubre = 0
    for ingreso_octubre in ingresos_octubre:
        total_octubre = total_octubre + ingreso_octubre
    
    #NOVIEMBRE--->  
    #Tomo los ids de las ventas por mes para compararlos con los ids y su precio
    ids_noviembre = list()
    for veces_noviembre in noviembre:
        ids_noviembre.append(veces_noviembre[1])
    #print(ids_noviembre)
    
    # Creo un reporte que me dice que ids si tuvieron ventas en el mes
    reporte_noviembre= list()
    for ids in range(len(id_lst)):
        count = 0
        for id_noviembre in range(len(ids_noviembre)):
            if (ids_noviembre[id_noviembre] == id_lst[ids]):
                count = count + 1
        
        reporte_noviembre.append(count) 
    #print(reporte_noviembre)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_noviembre = list()
    for price_noviembre in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_noviembre.append(prices[price_noviembre] * reporte_noviembre[price_noviembre])#precio del producto por el numero de ventas x producto
    #print(ingresos_noviembre)
    
    #Calculo de las ventas totales del mes de los ids
    total_noviembre = 0
    for ingreso_noviembre in ingresos_noviembre:
        total_noviembre = total_noviembre + ingreso_noviembre
    
    #DICIEMBRE--->  
    #Tomo los ids de las ventas por mes para compararlos con los ids y su precio
    ids_diciembre = list()
    for veces_diciembre in diciembre:
        ids_diciembre.append(veces_diciembre[1])
    #print(ids_diciembre))
    
    # Creo un reporte que me dice que ids si tuvieron ventas en el mes
    reporte_diciembre= list()
    for ids in range(len(id_lst)):
        count = 0
        for id_diciembre in range(len(ids_diciembre)):
            if (ids_diciembre[id_diciembre] == id_lst[ids]):
                count = count + 1
        
        reporte_diciembre.append(count) 
    #print(reporte_diciembre)
    
    #Multiplico cada uno de los ids con ventas por su precio correspondiente
    ingresos_diciembre = list()
    for price_diciembre in range(len(prices)):#ciclo para todos los precios de la lista
        ingresos_diciembre.append(prices[price_diciembre] * reporte_diciembre[price_diciembre])#precio del producto por el numero de ventas x producto
    #print(ingresos_diciembre)
    
    #Calculo de las ventas totales del mes de los ids
    total_diciembre = 0
    for ingreso_diciembre in ingresos_diciembre:
        total_diciembre = total_diciembre + ingreso_diciembre
    
    if option_8 == 1:
        print("\n""REVENUE by MONTH")
        print("Loading...")
        print("Results:")
        print("|--------------------------------------|")
        print("| TOTAL REVENUE JANUARY: $",total_enero,)
        print("|--------------------------------------|")
        print("| TOTAL REVENUE FEBRUARY: $",total_febrero,)
        print("|--------------------------------------|")
        print("| TOTAL REVENUE MARCH: $",total_marzo,)
        print("|--------------------------------------|")
        print("| TOTAL REVENUE ARIL: $",total_abril,)
        print("|--------------------------------------|")
        print("| TOTAL REVENUE MAY: $",total_mayo,)
        print("|--------------------------------------|")
        print("| TOTAL REVENUE JUNE: $",total_junio,)
        print("|--------------------------------------|")
        print("| TOTAL REVENUE JULY: $",total_julio,)
        print("|--------------------------------------|")
        print("| TOTAL REVENUE AUGUST: $",total_agosto,)
        print("|--------------------------------------|")
        print("| TOTAL REVENUE SEPTEMBER: $",total_septiembre,)
        print("|--------------------------------------|")
        print("| TOTAL REVENUE OCTOBER: $",total_octubre,)
        print("|--------------------------------------|")
        print("| TOTAL REVENUE NOVEMBER: $",total_noviembre,)
        print("|--------------------------------------|")
        print("| TOTAL REVENUE DECEMBER: $",total_diciembre,)
        print("|--------------------------------------|")

        continuar = input("new selection (yes/no): ")
        if continuar == "yes":
            print("loading...")
        elif continuar == "no":
            print("logggin out..")
               
        else: print("type: yes or no")
        continue
else:
    print("Disconecting... you typed:[no] or typed an error\n"
          "See you or try to log in again (TIP: yes/no)")

    

#----------------------------FINAL DE FINALES-------------------------------->