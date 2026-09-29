correos = ["santi@gmail","camilo","nico@gmail.com"]

validos = [correo for correo in correos if "@" in correo ]
print("correos validos", validos)