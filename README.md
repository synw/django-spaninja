# Django api server + single page app template

- **Api server** using [Django Ninja](https://github.com/vitalik/django-ninja)
- **Vitejs frontend** using [Vuejs](https://vuejs.org/)

## Features

- Auth and csrf protected api by default
- Auto generated api docs
- Django forms support
- Login and logout
- User registration with email confimation
- Responsive frontend with dark mode support

<details>
<summary>:books: Read the <a href="https://synw.github.io/django-spaninja">documentation</a></summary>

 - [Get started](https://synw.github.io/django-spaninja/get_started)
    - [Install and run](https://synw.github.io/django-spaninja/get_started/install_and_run)
    - [Write endpoints](https://synw.github.io/django-spaninja/get_started/write_endpoints)
    - [Build](https://synw.github.io/django-spaninja/get_started/build)
 - [Base app](https://synw.github.io/django-spaninja/base_app)
     - [Forms](https://synw.github.io/django-spaninja/base_app/forms)
        - [Usage](https://synw.github.io/django-spaninja/base_app/forms/usage)
     - [Schemas](https://synw.github.io/django-spaninja/base_app/schemas)
 - [Account app](https://synw.github.io/django-spaninja/account_app)
     - [Endpoints](https://synw.github.io/django-spaninja/account_app/endpoints)
     - [Schemas](https://synw.github.io/django-spaninja/account_app/schemas)
     - [Utilities](https://synw.github.io/django-spaninja/account_app/utilities)
         - [Email](https://synw.github.io/django-spaninja/account_app/utilities/email)
         - [Token](https://synw.github.io/django-spaninja/account_app/utilities/token)

</details>

<div align="center">
<img src="docsite/public/poneyninja.png" alt="" />
</div>

## Development 

### Code quality

This project uses [Pycheck](https://github.com/emencia/pycheck) to monitor the quality of the code. To install
the code quality tools:

```bash
make install-pycheck
# or
yarn global add @pycheck/cli
yarn global add @pycheck/ui
# or
npm install -g @pycheck/cli
npm install -g @pycheck/ui
```

#### Analysis and history

Run:

```bash
pycheckui
```

Open `localhost:5143` in a browser to run an analysis. Note: this uses a `.pycheck.db` local Sqlite file
to store the code quality history

#### Command line

To do a quick check in the command line (not recorded in history):

```bash
pycheck
```

