

function Assistant() {
    const { useState } = React

    const [name, setName] = useState("")
    const [topic, setTopic] = useState("")

    function handleSubmit(event) {
        event.preventDefault()
        console.log('Name', name)
    }

    return (
    <div>
        <p>I am your Assistant...</p>
        <form onSubmit={handleSubmit}>
            <input
                id='name'
                name='name'
                value={name}
                onInput={(event)=>setName(event.target.value)}>
            </input>
            <select>
                <option value="command">Command</option>
                <option value="lang-arb">Language: Arabic</option>
                <option value="lang-cmn">Language: Mandarin Chinese</option>
                <option value="lang-heb">Language: Hebrew</option>
            </select>
        </form>
    </div>
    )
}

ReactDOM.render(<Assistant/>, document.querySelector('#assistant'))
