const libName = "django-spaninja";
const libTitle = "Django Spaninja";
const repoUrl = "https://github.com/synw/django-spaninja";

const links: Array<{ href: string; name: string }> = [
  // { href: "/python", name: "Python api" },
];

// python runtime
const mylib = new URL(`/apps-0.2.0-py3-none-any.whl`, import.meta.url).href;
const pipPackages = ["sqlite3", "django", "django-ninja", mylib];
const pyodidePackages = [];
const examplesExtension = "py";

async function loadHljsTheme(isDark: boolean) {
  if (isDark) {
    await import("../node_modules/highlight.js/styles/base16/material-darker.css")
  } else {
    await import("../node_modules/highlight.js/styles/stackoverflow-light.css")
  }
}

/** Import the languages you need for highlighting */
import hljs from 'highlight.js/lib/core';
import python from 'highlight.js/lib/languages/python';
import bash from 'highlight.js/lib/languages/bash';
import typescript from 'highlight.js/lib/languages/typescript';
import xml from 'highlight.js/lib/languages/xml';
hljs.registerLanguage('python', python);
hljs.registerLanguage('typescript', typescript);
hljs.registerLanguage('bash', bash);
hljs.registerLanguage('html', xml);

// some Python code to run after install
const initCode = `import django
import os
from django.conf import settings
from django.core.management import call_command
from pathlib import Path
Path("urls.py").write_text("""\
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
"""
)
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
settings.configure(DEBUG=True, INSTALLED_APPS=[
  "django.contrib.contenttypes",
  "django.contrib.admin",
  "django.contrib.auth",
  "ninja"
], DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
  }
},
ROOT_URLCONF="urls") 
django.setup()
call_command("migrate")`

export {
  libName,
  libTitle,
  repoUrl,
  pipPackages,
  examplesExtension,
  pyodidePackages,
  links,
  hljs,
  initCode,
  loadHljsTheme
}