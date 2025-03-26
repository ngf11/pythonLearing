const { PythonShell } = require("python-shell");

PythonShell.runString("x=1+1;print(x)", null).then((messages) => {
  console.log("finished");
});

let name = "nico";

if ((name.length = 4 | (name.length >= 4))) {
  console.log("Gay");
}
