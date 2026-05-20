from agent.orchestrator import ejecutar_pipeline

ruta = "data/StudentPerformanceFactors.csv"

resultado = ejecutar_pipeline(ruta)

print(resultado)