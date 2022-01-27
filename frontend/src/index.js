import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from "react-router-dom";
import Root from "pages"; // pages/index.js가 import 됨
import "antd/dist/antd.css";
import './index.css';



ReactDOM.render(
    <BrowserRouter>
        <Root />
    </BrowserRouter>,
    document.getElementById('root')
);
