# 🏰 RealEstate CRM - Sistema de Gestión de Prospectos

**RealEstate CRM** es una aplicación web minimalista y robusta diseñada para la gestión eficiente de prospectos inmobiliarios de alto valor (*High-Ticket Real Estate*).

El sistema se centra en la velocidad operativa, permitiendo a equipos comerciales gestionar estados de venta, presupuestos y notas sin la complejidad de los CRMs tradicionales. Cuenta con soporte nativo **Bilingüe (Español/Inglés)** y una arquitectura de roles estricta.

---

##  Características Principales

* **Gestión de Prospectos:** Base de datos centralizada de clientes potenciales con filtros dinámicos por País y Estado.
* **Soporte Multi-Idioma:** Traducción instantánea de toda la interfaz (EN 🇺🇸 / ES 🇪🇸) persistente por sesión de usuario.
* **Workflow Comercial Visual:**
    * Estados claros con código de color: 🔴 No Contactado, 🟡 Pendiente, 🟢 Interesado, ⚫ No Interesado.
    * Clasificación de Presupuesto: 10M, 6M, 4M. de dolares!!
* **Automatización:** Registro automático de la fecha de "Último Contacto" al cambiar el estado del prospecto.
* **UI Moderna:** Interfaz limpia basada en **Bootstrap 5** con iconos **FontAwesome**

---

## 👥 Roles y Permisos

El sistema utiliza un modelo de seguridad jerárquico para proteger la integridad de los datos.

| Rol | Perfil Técnico | Responsabilidad | Permisos |
| :--- | :--- | :--- | :--- |
| **Data Entry** | `data_entry` | Administrador de Datos | **Control Total.** Es el único que puede crear nuevos prospectos, eliminar registros basura y corregir datos personales (Nombre, Email, País). |
| **Sales Agent** | `sales` | Agente Comercial | **Gestión de Venta.** Visualiza toda la lista. Solo puede editar el Estado, el Presupuesto y las Notas de bitácora. No puede borrar ni crear. |
| **Investor** | `investor` | Auditor / Dueño | **Solo Lectura.** Acceso total a la visualización de datos y filtros para auditar el negocio, sin permisos de edición. |

---

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.10+ / Django 5.x
* **Base de Datos:**
    * 
    * *Producción:* MySQL 
* **Frontend:** HTML5, CSS3, Bootstrap 5 (CDN).
* **Infraestructura:** Listo para desplegar en PythonAnywhere.

---

## ⚙️ Instalación Local

Sigue estos pasos para levantar el proyecto en tu máquina:

### 1. Clonar el repositorio
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd realstate
las credenciales estan en otro archivo por seguridad, el que hace el crud es el data entry, 