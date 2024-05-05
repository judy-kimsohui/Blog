declare module "*.scss" {
  const content: string
  export = content
}

declare module '*.png' {
  const content: string;
  export default content;
}

// dom custom event
interface CustomEventMap {
  nav: CustomEvent<{ url: FullSlug }>
  themechange: CustomEvent<{ theme: "light" | "dark" }>
}

declare const fetchData: Promise<ContentIndex>
