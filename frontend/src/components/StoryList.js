import React from "react";
import { Card } from "antd";
import "./StoryList.scss";

export default function StoryList( { style }) {
    return (
        <div style={style}>
            <Card title="stories" size="small">
                Stories 입니다.
            </Card>
        </div>
    );
}