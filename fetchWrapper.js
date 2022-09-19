export default class FetchWrapper {
    constructor(baseURL) {
        this.baseURL = baseURL;
    }

    get(endpoint) {
        return fetch(this.baseURL + endpoint)
            .then(response => response.json());
    }

    put(endpoint, body) {
        return this._send("put", endpoint, body);
    }

    post(endpoint, body) {
        return this._send("post", endpoint, body);
    }

    delete(endpoint, body) {
        return this._send("delete", endpoint, body);
    }

    _send(method, endpoint, body) {
        return fetch(this.baseURL + endpoint, {
            method,
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(body)
        }).then(response => response.json());
    }
}

/*
import FetchWrapper from './fetch-wrapper.js'
const updateUserProfile = (firstName, lastName) => {
    // TODO
    const API = new FetchWrapper('https://api.learnjavascript.online/demo/');
    API.post('user.json', {
        firstName : firstName,
        lastName: lastName
    }).then(data => console.log(data))
}
*/

/*import FetchWrapper from './fetch-wrapper.js'
const getChapters = () => {
    // TODO
    const API = new FetchWrapper("https://jsdemo-3f387-default-rtdb.europe-west1.firebasedatabase.app/chapters");
    API.get('/all.json').then(data => {
        console.log(data)
        let isCompleted = data.filter(data => data.isCompleted)
        displayCompletedChapters(isCompleted)
    })
}*/