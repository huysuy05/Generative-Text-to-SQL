document.addEventListener("DOMContentLoaded", function() {
    const setSchemaButton = document.getElementById("setSchemaButton");
    const generateQueryButton = document.getElementById("generateQueryButton");
    const executeQueryButton = document.getElementById("executeQueryButton");
    const executedQueryContent = document.getElementById("executed-query-content");
    const chatBox = document.getElementById("chat-box-id");

    setSchemaButton.addEventListener("click", function(event) {
        event.preventDefault();
        const schemaContent = document.getElementById("schema").value;

        fetch('http://localhost:5500/set_schema', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({ schema: schemaContent })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    generateQueryButton.addEventListener("click", function(event) {
        event.preventDefault();
        const questionContent = document.getElementById("textInput").value;

        fetch('http://localhost:5500/gen_query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: questionContent })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            executedQueryContent.value = data.query;
            executedQueryContent.removeAttribute("readonly");
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    executeQueryButton.addEventListener("click", function(event) {
        event.preventDefault();
        const query = executedQueryContent.value;

        fetch('http://localhost:5500/exec_query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ query: query })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            chatBox.innerHTML = '';

            const result = data.result;

            if (result.length > 0) {
                const table = document.createElement("table");
                table.classList.add("data-table");

                const headers = Object.keys(result[0]);
                const thead = document.createElement("thead");
                const headerRow = document.createElement("tr");

                headers.forEach(header => {
                    const th = document.createElement("th");
                    th.textContent = header;
                    headerRow.appendChild(th);
                });

                thead.appendChild(headerRow);
                table.appendChild(thead);

                const tbody = document.createElement("tbody");

                result.forEach(item => {
                    const row = document.createElement("tr");
                    headers.forEach(header => {
                        const td = document.createElement("td");
                        td.textContent = item[header] !== null ? item[header] : "";
                        row.appendChild(td);
                    });
                    tbody.appendChild(row);
                });

                table.appendChild(tbody);
                chatBox.appendChild(table);
            } else {
                const noResultMessage = document.createElement("div");
                noResultMessage.textContent = "No results found.";
                chatBox.appendChild(noResultMessage);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
