#crear la clase Te
class Te:
    #atributos de clase
    sabores= ['te negro', 'te verde', 'agua de hierbas']
    formatos = {'300gr': 3000, '500gr': 5000}
    min_preparacion = {'te negro': 3, 'te verde': 5, 'agua de hierbas': 6}
    uso = {'te negro': 'al desayuno', 'te verde': 'al medio dia', 'agua de hierbas': 'al atardecer'}
    vigencia = 365
    
    # # met para obtener el tiempo de preparación, recomendación y precio
    # def obtener_datos_tea(self, sabor, formato):
    #     if sabor not in self.sabores and formato not in self.formatos:
    #         return "Error: sabor o formato no valido."

    #     precio = self.formatos=[formato]
    #     tiempo_preparacion = self.min_preparacion[sabor]
    #     recomendacion = self.uso[sabor]

    #     return f"sabor: {sabor}\n *formato: {formato}\n *tiempo de preparación: {tiempo_preparacion} minutos\n * Recomendación de consumo: {recomendacion}\n *precio: ${precio}"
    @staticmethod
    def obtener_datos_por_sabor(sabor_numero):
        sabores_numero = {1: 'te negro', 2: 'te verde', 3: 'agua de hierbas'}
        if sabor_numero not in sabores_numero:
            return "error: num de sabor no valido"

        sabor = sabores_numero[sabor_numero]
        tiempo_preparacion = Te.min_preparacion[sabor]
        recomendacion = Te.uso[sabor]

        return f" * sabor: {sabor}\n * tiempo de preparacion: {tiempo_preparacion} minutos\n * recomendacion de consumo: {recomendacion}"

    @staticmethod
    def precio_formato(formato_numero):
        formatos_numero = {0: '300gr', 1: '500gr'}

        if formato_numero not in formatos_numero:
            return "error: num de formato no valido"

        formato = formatos_numero[formato_numero]
        precio = Te.formatos[formato]

        return f" * formato: {formato}\n * precio: ${precio}"
