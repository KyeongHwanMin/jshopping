import React, { useState, useEffect } from "react";
import Axios from "axios";

const apiUrl = "http://localhost:8000/products/products/";

function ProductList() {
const [ProductList, setProductList] = useState([]);
    useEffect(() => {
        Axios.get(apiUrl)
            .then(response => {
                const { data } = response;
                console.log("loaded response :", response);
                setProductList(data);
            })
            .catch(error => {
                // error.response;
            });
        console.log("mounted");
        }, []);

        return (
            <div>
                <h1>ProductList</h1>
                {ProductList.map( product =>{
                    const { id, name, price, image } = product;
                    return (
                        <div key ={id}>
                            {name}, {price}
                            <img src={image} alt={name} style={{ width: "100px" }} />
                        </div>
                    );
                }

                )}
            </div>
        );
}

export default ProductList;