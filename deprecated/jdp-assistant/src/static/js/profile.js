

function App() {
    const { useState, useEffect } = React

    const [password, setPassword] = useState("")
    const [langctx, setLangCtx] = useState("heb")
    const [languages, setLanguages] = useState([])

    function handleSubmit(event) {
        event.preventDefault()
        console.log('Name', name)
    }

    const client = axios.create({
        baseURL: "https://jsonplaceholder.typicode.com/posts" 
    });

    useEffect(() => {
        client
        .get('?_limit=10')
        .then((response) => {
            setLanguages([{"id":"1", "title":"Test"}]);
            console.log(languages)
         });
    }, [])

    return (
    <div>
        <form onSubmit={handleSubmit}>
            <label for="password">Password</label>
            <input
                type="password"
                name="password"
                id="password"
                value={password}
                onInput={(event)=>setPassword(event.target.value)} />

            <label for="langctx">Language context</label>
            <select
                name="langctx"
                id="langctx"
                value={langctx}
                onInput={(event)=>setLangCtx(event.target.value)}>
                <option value="arb">Arabic</option>
                <option value="cmn">Mandarin Chinese</option>
                <option value="heb">Hebrew</option>
                {languages.map((lang) => {
                    <option value="{lang.id}">{lang.name}</option>
                })}
            </select>
        </form>
    </div>
    )
}

const root = ReactDOM.createRoot(document.getElementById('app'));
root.render(<App />)
