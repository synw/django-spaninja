<template>
  <img class="absolute top-0 left-0 z-0 w-full h-screen" src="@/assets/img/home.png" alt="" />
  <div class="w-full">
    <div class="relative w-full h-full text-center">
      <div class="absolute left-0 flex flex-col items-center justify-center w-full h-full top-64 sm:top-96">
        <div class="p-3 text-white text-7xl mb-28">
          Just <span class="font-bold txt-success">code</span> your endpoints
        </div>
        <div v-if="!user.isLoggedIn.value === true">
          <button class="py-3 text-lg btn success" @click="$router.push('/account')">Create an account</button>
          <button class="py-3 ml-5 text-lg font-bold text-white border-white btn"
            @click="$router.push('/login')">Login</button>
        </div>
        <div v-else>
          <button class="py-3 text-lg btn primary" @click="$router.push('/page')">Example page</button>
          <button class="py-3 ml-5 text-lg font-bold text-white border-white btn" @click="logout()">Logout</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { user } from '@/state';
import { logout } from '@/auth';
</script>