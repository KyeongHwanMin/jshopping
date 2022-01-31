import React, { createContext } from "react";

const initialState = {
 jwtToken: "",
};

const AppContext = createContext(initialState); // 디폴트

const reducer = (prevState, action) => {
    return prevState;
};

export const AppProvider = ({ children }) => { // 외부에서 사용할 수 있게 설정
    const [store, dispatch] = useReducer(reducer, initialState);
    return (
        <AppContext.Provider value = {{ store, dispatch}}>
            {children}
        </AppContext.Provider>
    );
};

export const useAppContext = () => useContext(AppContext);

