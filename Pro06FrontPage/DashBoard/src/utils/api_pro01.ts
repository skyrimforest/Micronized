import PREFIXES  from "./device";
const URL_PREFIX = PREFIXES.CLOUD_PREFIX+":12000/";
const APIS_PRO01:{[key:string]:string} = {
    pro01test:"test",
    pro01sendtest:"pics/test",
    pro01sendpics:"pics/sendpics",
}

for (const i in APIS_PRO01) {
    APIS_PRO01[i] = URL_PREFIX + APIS_PRO01[i];
}

export default APIS_PRO01

