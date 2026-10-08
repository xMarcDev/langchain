# Proyecto LangChain

Entorno de pruebas con LangChain, OpenAI, Google Gemini y Streamlit.

- Python: 3.12
- Entorno virtual: `venv/`

## 1. Habilitar scripts en PowerShell

Por defecto Windows bloquea la ejecución de scripts `.ps1`, y eso impide activar el
entorno virtual (`venv\Scripts\Activate.ps1`). Se soluciona una sola vez, sin permisos
de administrador:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

`RemoteSigned` permite ejecutar scripts locales y exige firma digital solo a los
descargados de internet.

## 2. Crear y activar el entorno virtual

Si el entorno todavía no existe:

```powershell
python -m venv venv
```

Activarlo:

```powershell
venv\Scripts\activate
```

El prompt queda así cuando está activo:

```
(venv) PS C:\Users\ACER\Desktop\IA\langchain>
```

Para salir: `deactivate`.

## 3. Instalar las dependencias

Con el entorno activado:

```powershell
pip install -U pip
pip install -r requirements.txt
```

Sin activar el entorno, apuntando directamente al Python del venv:

```powershell
venv\Scripts\pip.exe install -r requirements.txt
```

Dependencias declaradas en `requirements.txt`:

| Paquete | Para qué sirve |
| --- | --- |
| `langchain` | Núcleo del framework (cadenas, prompts, agentes) |
| `langchain-openai` | Integración con los modelos de OpenAI (GPT) |
| `langchain-google-genai` | Integración con los modelos de Google (Gemini) |
| `streamlit` | Interfaz web para las demos |

Para actualizar todo a la última versión:

```powershell
pip install -U -r requirements.txt
```

Si más adelante quieres congelar las versiones exactas que tienes instaladas:

```powershell
pip freeze > requirements.txt
```

## 4. Configurar las claves de API

Las claves **nunca** se escriben en el código. Se definen como variables de entorno.

Solo para la sesión actual de PowerShell:

```powershell
$env:OPENAI_API_KEY = "sk-..."
$env:GOOGLE_API_KEY = "..."
```

De forma permanente para tu usuario:

```powershell
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sk-...", "User")
[Environment]::SetEnvironmentVariable("GOOGLE_API_KEY", "...", "User")
```

Después de la opción permanente hay que cerrar y volver a abrir PowerShell.

## 5. Ejecutar

Scripts de ejemplo (Tema1):

```powershell
python Tema1\01_invocar_chat_model.py
python Tema1\02_prompt_template_con_lcel.py
```

Scripts de ejemplo (Tema2), no necesitan API key:

```powershell
python Tema2\01_runnable_lambda_encadenado.py
python Tema2\04_prompt_template_format.py
python Tema2\05_chat_prompt_template_format_messages.py
python Tema2\07_messages_placeholder_historial.py
python Tema2\08_role_prompt_templates.py
python Tema2\09_pydantic_validacion_basica.py
```

Scripts de ejemplo (Tema2) que sí necesitan `OPENAI_API_KEY`:

```powershell
python Tema2\10_structured_output_pydantic.py
python Tema2\11_structured_output_parser.py
```

Aplicación Streamlit:

```powershell
streamlit run Tema1/03_chatbot_streamlit_con_historial.py
streamlit run Tema1/04_chatbot_streamlit_mensajes_directos.py
```
