# Analisis M/M/1/K/∞ y comprobación/comparación con Netlogo y Mesa

1) Parametros:

   - λ: Equivale a la tasa de llegadas
   - μ: Tasa de servicio (generalmente 1/s)
   - 1: Un solo servidor
   - K: Capacidad total del sistema (clientes en servivio + en cola). Si llega un cliente cuando ya hay K clientes, es rechazado (pérdida).
   - Fuente infinita: la tasa de llegada no depende del número de clientes en el sistema.

2) Probabilidades:

   - Para p distinto de 1:

     <img width="299" height="35" alt="imagen_2025-09-23_224659382" src="https://github.com/user-attachments/assets/32e5637b-8e99-467e-896c-18b6ada0780c" />

     donde P(0) se obtiene por normalización (para que el resultado sea 1):

     <img width="169" height="51" alt="image" src="https://github.com/user-attachments/assets/9b46263e-7f66-4456-9281-48eb9848fe05" />


   - Probabilidad de bloqueo (con sistema lleno):
  
     <img width="177" height="40" alt="image" src="https://github.com/user-attachments/assets/9796872d-e103-4c2f-96d4-ab739e0ecc2e" />

   - Caso de p=1 (con n = 0,..., K)

     <img width="142" height="48" alt="image" src="https://github.com/user-attachments/assets/d3db5839-b58f-4f3d-930f-0a5c979e2a99" />

   - Tasa de llegada (solo entran al sistema aquellas llegadas que encuentran espacio):

     <img width="162" height="28" alt="Screenshot 2025-09-23 225623" src="https://github.com/user-attachments/assets/130bf47c-34df-48c5-ba68-46265329bb8d" />

   - Probabilidad de servidor ocupado:

     <img width="60" height="25" alt="imagen_2025-09-23_230501656" src="https://github.com/user-attachments/assets/be3c5ba3-1ed8-4440-8765-384656a89fcb" />



3) Numero medio en el sistema L (Ns):
   
   - Para p diferente de 1 existe la formula:

       <img width="392" height="68" alt="image" src="https://github.com/user-attachments/assets/a7a73bf6-55f6-467a-b605-51806f20b0cf" />

     Mientras que para p=1 existe:

       <img width="97" height="61" alt="image" src="https://github.com/user-attachments/assets/ef889434-1eb9-4b7b-81c1-df119e0c052e" />

   - Numero medio en cola (Nw):

     L - (1 - P(0)),
     Ya que la probabilidad de que el servidor este ocupado es de 1-P(0)

   - Tiempos medios:

     - Para calcularlos, usamos la tasa de llegada cuando hay bloqueo (Lambda eff)

        <img width="105" height="49" alt="imagen_2025-09-23_231250748" src="https://github.com/user-attachments/assets/b12846b1-e31a-4692-b7f2-3dbeb31ba8a0" />

        <img width="121" height="54" alt="image" src="https://github.com/user-attachments/assets/ffba93aa-8532-46b8-bc2c-24f660806669" />


4) Simulación en NetLogo:

   - λ = mean-arrival-rate = 0.95 (por tick)
   - μ = mean-service-time = 1.45
   - Un unico servidor (1)

      <img width="910" height="595" alt="imagen_2025-09-23_232904924" src="https://github.com/user-attachments/assets/67046da5-8ecf-42c1-858f-572c92ccc20f" />

   - Calculos de acuerdo al modelo (con K=5 para tener un sistema estable):
  
     - Calculo de P(0)

      <img width="199" height="69" alt="imagen_2025-09-23_233907651" src="https://github.com/user-attachments/assets/90702b2d-80a0-4488-bd39-e0b2488eab15" />
  
      - Calculo de P(k)

      <img width="537" height="48" alt="imagen_2025-09-23_233525566" src="https://github.com/user-attachments/assets/68fa5e27-dc75-4e07-a272-affe19349634" />
  
      - Tasa efectiva de entrada:
     
      <img width="399" height="21" alt="imagen_2025-09-23_234115542" src="https://github.com/user-attachments/assets/df2a6c85-d4d1-4ab1-b737-7c4bbddb92d6" />


     - Tiempos medios:

      <img width="443" height="51" alt="imagen_2025-09-23_233713985" src="https://github.com/user-attachments/assets/aca12e46-4599-4145-8178-2877267a6483" />

5) Comprobación con codigo estilo MESA:

  -  Para realizar esta comprobación, usaremos el codigo encontrado en el archivo "mm1k.py", el cual servira para validar los resultados anteriormente obtenidos. Es importante decir que los resultados seran aproximados, pues los valores obtenidos con los calculos basados en modelos matematicos se tratan de predicciones. Para correr este codigo solo es necesario tener python instalado en el equipo y asegurarse de que el Comand Prompt esta analizando la carpeta en la cual tenemos descargado "mm1k.py", una vez confirmado solo ejecutamos el siguiente comando:

     <img width="167" height="24" alt="imagen_2025-09-24_000421296" src="https://github.com/user-attachments/assets/4066e65e-abc1-4373-ada4-b1b2193a348f" />

     Una vez hecho esto, nos mostrara los resultados:

     <img width="328" height="153" alt="imagen_2025-09-24_000525827" src="https://github.com/user-attachments/assets/e52f88c2-3322-4dac-b2a1-8a9281cbb0c0" />

     Al comparar estos valores con los obtenidos anteriormente con el modelo, vemos que coinciden de forma exacta en unos casos y de forma muy cercana en otros, por lo cual podemos concluir que el modelo matematico es valido.


   
   







    




   
      


  
     
