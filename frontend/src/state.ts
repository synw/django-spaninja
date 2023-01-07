import { useApi } from "restmix";
import { useScreenSize } from "@snowind/state";
import { User } from "@snowind/state";
import { initNotifyService } from "@/notify";

const serverUrl = import.meta.env.DEV ? "http://localhost:8000" : "";

let setStateReady: (value: unknown) => void;
let isStateReady = new Promise((r) => setStateReady = r);

const user = new User();
const api = useApi({
  serverUrl: serverUrl
});
const { isMobile, isTablet, isDesktop } = useScreenSize();

function initState() {
  initNotifyService()
}

async function initUserState() {
  const res = await api.get<{ is_connected: boolean, username: string }>("/api/account/state");
  if (res.data.is_connected) {
    user.isLoggedIn.value = true
  }
  user.name.value = res.data.username;
  api.setCsrfTokenFromCookie();
  setStateReady(true);
}


export {
  user,
  api,
  serverUrl,
  isMobile,
  isTablet,
  isDesktop,
  isStateReady,
  initUserState,
  initState,
}
