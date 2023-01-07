import { ShallowUnwrapRef } from "vue";
import { api } from "@/state";
import { FormErrors } from "@/interfaces";
import { ApiResponse } from "restmix";

function processFormErrors(formErrors: FormErrors): Record<string, string> {
  const errors: Record<string, string> = {};
  for (const [name, errs] of Object.entries(formErrors)) {
    let msgs = new Array<string>();
    errs.forEach((err) => {
      msgs.push(err.message)
    })
    errors[name] = msgs.join("<br />");
  }
  return errors
}

async function postFormData<T = Record<string, any>>(
  form: ShallowUnwrapRef<{ errors: Record<string, string> }>,
  uri: string,
  data: any,
  put: boolean = false
): Promise<{ ok: boolean, data?: T, res?: ApiResponse<T> }> {
  let resp: ApiResponse<T>;
  if (!put) {
    // console.log("POST", uri, JSON.stringify(data, null, "  "));
    resp = await api.post<T>(uri, data);
  } else {
    resp = await api.put<T>(uri, data);
  }
  if (!resp.ok) {
    switch (resp.status) {
      case 418:
        const errs = JSON.stringify(resp.data["detail"], null, "  ");
        throw new Error(`418 Invalid form data ${errs}`)
      case 422:
        //console.log("RESP", JSON.stringify(resp.data, null, "  "))
        const errors = resp.data["errors"] as FormErrors;
        form.errors = processFormErrors(errors);
        return { ok: false }
      default:
        const err = JSON.stringify(resp.data["detail"], null, "  ");
        console.log(`Unmanaged error code ${resp.status}, ${err}`)
        return { ok: false, res: resp }
      //throw new Error(`Unmanaged error code ${resp.status}, ${resp}`)
    }
  }
  //console.log("RESP", JSON.stringify(resp, null, "  "))
  return { ok: true, data: resp.data }
}

async function putForm<T = Record<string, any>>(
  form: ShallowUnwrapRef<{ errors: Record<string, string> }>,
  uri: string, formData: Record<string, any>
): Promise<{ ok: boolean, data?: T, res?: ApiResponse<T> }> {
  return await postFormData<T>(form, uri, formData, true)
}

async function postForm<T = Record<string, any>>(
  form: ShallowUnwrapRef<{ errors: Record<string, string> }>,
  uri: string, formData: Record<string, any>
): Promise<{ ok: boolean, data?: T, res?: ApiResponse<T> }> {
  return await postFormData<T>(form, uri, formData)
}

export { postForm, putForm, postFormData }