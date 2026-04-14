const API_BASE_URL = "http://127.0.0.1:8000";

async function encode_request(input_path, output_path){

    return await fetch(`${API_BASE_URL}/main/encode`, {
           method: "POST",
           headers: {
               "Content-Type": "application/json"
           },
           body: JSON.stringify({
               input_path: input_path,
               output_path: output_path
           })
       });

}

async function submit_handler(e) {
    e.preventDefault();

    const data = new FormData(e.target);

    const response = await encode_request(
        data.get("input_path"),
        data.get("output_path")
    );

    const result = await response.json();
    console.log(result);
}

document
    .getElementById("halbanot-form")
    .addEventListener("submit", submit_handler);