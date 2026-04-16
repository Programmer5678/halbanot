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

async function decode_request(input_path, output_path){

    return await fetch(`${API_BASE_URL}/main/decode`, {
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

function get_request_func(button_value){
    switch( button_value ){
        case("encode") : return encode_request;
        case("decode") : return decode_request;
        default: alert("submit button value should be encode or decode")
    }

}

async function submit_handler(e) {
    e.preventDefault();

    const data = new FormData(e.target);
    const request_func = get_request_func(e.submitter?.value);

    const response = await request_func(
        data.get("input_path"),
        data.get("output_path")
    );


    document.getElementById("response_code").innerText = response.status
    document.getElementById("response_success").innerText = response.ok ? "SUCCESS" : "FAIL"

    const result_str = JSON.stringify( await response.json() );
    document.getElementById("response_json").innerText = result_str;

}

document
    .getElementById("halbanot-form")
    .addEventListener("submit", submit_handler);