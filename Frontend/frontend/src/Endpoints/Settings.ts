import axios from 'axios';


export const BASE_URL = 'https://na-mahlzeit.de/api'
//export const BASE_URL = "http://localhost:8000/api"


const instance = axios.create({
    baseURL: BASE_URL,
    withCredentials: true,
})

export async function fetchCsrfToken() {
    const response = await instance.get("/get_csrf_token");
    return response.data.csrfToken;
}
