<template>
  <form-card class="mx-3">
    <div class="hidden text-3xl text-center lg:block">Login</div>
    <div class="lg:pt-8">
      <span class="p-float-label">
        <InputText id="username" type="text" v-model="username" />
        <label for="username">Username</label>
      </span>
      <small v-if="'username' in form.errors" id="username-help" class="p-error" v-html="form.errors.username"></small>
    </div>
    <div class="mt-5">
      <span class="p-float-label">
        <Password v-model="password" :feedback="false" />
        <label for="password">Password</label>
      </span>
      <small v-if="'password' in form.errors" id="password-help" class="p-error" v-html="form.errors.password"></small>
    </div>
    <div class="pt-5 text-center">
      <button class="w-full btn bord-background success" @click="postLogin()">Login</button>
      <button class="mt-5 btn txt-light" @click="$router.back()">Cancel</button>
    </div>
  </form-card>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import FormCard from '@/widgets/FormCard.vue';
import router from '@/router';
import { postForm } from '@/forms';
import { user } from '@/state';
import { msg } from '@/notify';

const username = ref();
const password = ref();

const form = reactive<{ errors: Record<string, string> }>({ errors: {} });

async function postLogin() {
  const { ok, res } = await postForm(form, "/api/account/login", {
    username: username.value,
    password: password.value,
  });
  if (ok) {
    console.log("Login ok");
    user.name = username.value;
    user.isLoggedIn.value = true;
    msg.success("Ok", `User ${user.name} is logged in`)
    router.push("/")
  } else {
    if (res?.status == 401) {
      msg.warn("Login error", res.data["message"], 60000)
    }
    else if ("__all__" in form.errors) {
      //console.log("ERRS", form.errors)
      msg.warn("Login error", form.errors["__all__"], 60000)
    }
  }
}
</script>

