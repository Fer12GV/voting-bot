# backend/scraper.py
import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from constants import *

async def votar(playwright, intento):
    print(f"\n🔁 Intento {intento + 1} de {VOTE_ATTEMPTS}")
    browser = await playwright.chromium.launch(headless=True)  # <- CAMBIADO
    context = await browser.new_context()
    page = await context.new_page()

    try:
        print(f"🟢 Navegando a {URL_INICIAL}")
        await page.goto(URL_INICIAL)

        print("➡️ Haciendo clic en el botón 'Votar' de la portada...")
        await page.wait_for_selector(f"text={TEXTO_BTN_VOTAR}")
        await page.click(f"text={TEXTO_BTN_VOTAR}")

        print("⏳ Esperando redirección...")
        await page.wait_for_url("**/votos", timeout=10000)

        print("✅ Redireccionado. Haciendo clic en la categoría...")
        await page.wait_for_selector(f"text={TEXTO_CATEGORIA}")
        await page.click(f"text={TEXTO_CATEGORIA}")

        print("⏳ Esperando que las tarjetas estén presentes...")
        await page.wait_for_selector("div.cuadrado", state="attached", timeout=15000)

        print(f"🔍 Buscando empresa '{TEXTO_EMPRESA}'...")
        tarjetas = await page.query_selector_all("div.cuadrado")

        for tarjeta in tarjetas:
            nombre = await tarjeta.query_selector("h2.nombre-postulado")
            if nombre:
                texto = (await nombre.inner_text()).strip().upper()
                if texto == TEXTO_EMPRESA:
                    print(f"✅ Empresa encontrada: {texto}. Intentando votar...")
                    boton = await tarjeta.query_selector("button.btnvotar")
                    if boton:
                        await boton.click()
                        print("🎉 ¡Voto enviado con éxito!")
                        await page.wait_for_selector('div.modal-footer >> text="Aceptar"', timeout=5000)
                        await page.click('div.modal-footer >> text="Aceptar"')
                        print("✅ Modal de confirmación cerrado correctamente.")
                        await asyncio.sleep(2)
                    else:
                        print("⚠️ Botón de votar no encontrado.")
                    break
        else:
            print("❌ Empresa no encontrada.")

    except PlaywrightTimeoutError as e:
        print(f"⛔ Timeout durante la ejecución: {e}")
    except Exception as e:
        print(f"🔥 Error inesperado: {e}")
    finally:
        await browser.close()
        print("🧹 Navegador cerrado.")

async def ejecutar_votaciones(intentos):
    print(f"🚀 Iniciando proceso de votación con {intentos} intento(s)...")
    async with async_playwright() as playwright:
        for i in range(intentos):
            await votar(playwright, i)
    print("✅ Todos los intentos finalizados.")
