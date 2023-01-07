interface FormError {
  message: string;
  code: string;
}

type FormErrors = Record<string, Array<FormError>>;

export {
  FormError,
  FormErrors,
}