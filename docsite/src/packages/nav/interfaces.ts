interface CodeBlockRaises {
  description: string;
  type: string;
}

interface CodeBlockParam {
  description: string;
  type: string;
  default: string | null;
}

interface ExampleParam {
  code: string;
  is_executable: boolean;
}

interface ParsedDocstring {
  funcdef: string;
  description: string;
  long_description: string | null;
  example: ExampleParam | null;
  params: Record<string, CodeBlockParam>;
  raises: Array<CodeBlockRaises>;
  returns: Record<string, string> | null;
  extra_examples?: Array<ExampleParam>;
  extra_md?: {
    header: string,
    footer: string
  }
}

interface BaseNavItem {
  name: string;
  title: string;
  url: string;
  docpath: string;
}

interface DirNavItem extends BaseNavItem {
  has_md_index: boolean;
}

interface NavItem extends BaseNavItem {
  type: "markdown" | "component" | "directory"
}

interface DirNavListing extends DirNavItem {
  content: Array<NavItem>;
  docstrings: Array<DirNavItem>;
  children?: Array<DirNavListing>;
}

interface RouteDataPayload {
  name: string;
  title: string;
  hasMarkdown: boolean;
  hasDocstring: boolean;
  markdown: string;
  docstring: ParsedDocstring;
  node: DirNavListing;
  autoIndex: boolean;
}

export {
  CodeBlockParam,
  CodeBlockRaises,
  ExampleParam,
  ParsedDocstring,
  DirNavItem,
  NavItem,
  DirNavListing,
  RouteDataPayload,
}