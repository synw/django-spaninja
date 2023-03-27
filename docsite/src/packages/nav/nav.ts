import { useApi } from "restmix";
import { DirNavListing, ParsedDocstring, RouteDataPayload } from "./interfaces";
import { useDocloader } from "./loader";


function _routePathAsArray(routePath: string): Array<string> {
  const _routePathArray = new Array<string>();
  if (routePath.includes("/")) {
    if (routePath.startsWith("/")) {
      _routePathArray.push(...routePath.split("/").slice(1))
    } else {
      _routePathArray.push(...routePath.split("/"))
    }
  } else {
    _routePathArray.push(routePath)
  }
  return _routePathArray
}

const useNav = (docloader: ReturnType<typeof useDocloader>, api: ReturnType<typeof useApi>) => {
  let setReady: (value: unknown) => void;
  let onReady = new Promise((r) => setReady = r);
  let _tree = {} as DirNavListing;

  const _loadNav = async (): Promise<DirNavListing> => {
    let url = `/doc/nav.json`;
    const res = await api.get<DirNavListing>(url);
    if (res.ok) {
      return res.data
    }
    throw new Error(`${res.status}: ${res.data}`)
  }

  const init = async () => {
    _tree = await _loadNav();
    setReady(true);
  };

  const _findNodeFromRoutePathArray = (_routePathArray: string[]): DirNavListing => {
    let node = _tree;
    let children = _tree.children;
    //console.log("Route path array", _routePathArray, children);
    let i = 1;
    for (const segment of _routePathArray) {
      if (children) {
        const newnode = children?.find((c) => c.name == segment);
        if (!newnode) {
          return node
          //throw new Error(`Route path error: no ${segment} segment`)
        }
        // console.log("SET NODE", newnode)
        node = newnode;
        children = node?.children;
      } else {
        if (i == _routePathArray.length) {
          return node
        }
        throw new Error(`Route path error: children for ${segment} not found`)
      }
      ++i
    }
    return node
  };

  const findNode = (routePath: string): DirNavListing => _findNodeFromRoutePathArray(_routePathAsArray(routePath));

  const loadFromRoutePath = async (routePath: string): Promise<RouteDataPayload> => {
    await onReady;
    const _routePathArray = _routePathAsArray(routePath)
    const node = _findNodeFromRoutePathArray(_routePathArray);
    const lastSegment = _routePathArray.slice(-1)[0];
    if ((lastSegment == node.name) || lastSegment == "") {
      // this is a directory url, fetch the markdown index
      if (node.has_md_index) {
        const data = await docloader.loadMarkdown(node.docpath + "/index.md");
        return {
          name: lastSegment,
          title: node.title,
          hasMarkdown: true,
          hasDocstring: false,
          markdown: data,
          docstring: {} as ParsedDocstring,
          node: node,
          autoIndex: false,
        }
      } else {
        return {
          name: lastSegment,
          title: node.title,
          hasMarkdown: false,
          hasDocstring: false,
          markdown: "",
          docstring: {} as ParsedDocstring,
          node: node,
          autoIndex: true,
        }
      }
    }
    let hasMarkdown = false;
    let hasDocstring = false;
    let markdown = "";
    let title = node.title;
    // markdown content
    if (node.content.length > 0) {
      let mdNode = node.content.find(n => n.name == lastSegment);
      if (mdNode) {
        hasMarkdown = true;
        title = mdNode.title;
        markdown = await docloader.loadMarkdown(mdNode.docpath);
      }
    }
    //docstrings content
    let docstring = {} as ParsedDocstring;
    if (node.docstrings.length > 0) {
      const _docstring = await docloader.loadDocstrings(node.docpath);
      const _ds = _docstring[lastSegment];
      if (_ds) {
        hasDocstring = true;
        docstring = _ds;
      }
    }
    return {
      name: lastSegment,
      title: title,
      hasMarkdown: hasMarkdown,
      hasDocstring: hasDocstring,
      markdown: markdown,
      docstring: docstring,
      node: node,
      autoIndex: false,
    }
  }

  return {
    get tree() { return _tree },
    init,
    loadFromRoutePath,
    findNode,
  }
}

export { useNav }