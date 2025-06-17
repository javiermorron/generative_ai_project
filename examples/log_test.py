from utils.logger import logger

def test_log():
    logger.debug("🛠️ Este es un mensaje DEBUG (solo visible si el nivel es DEBUG).")
    logger.info("✅ Este es un mensaje INFO: el sistema de logs está funcionando.")
    logger.warning("⚠️ Este es un mensaje WARNING: algo podría salir mal.")
    logger.error("❌ Este es un mensaje ERROR: hubo un problema.")
    logger.critical("🚨 Este es un mensaje CRITICAL: la app podría fallar.")

if __name__ == "__main__":
    test_log()
