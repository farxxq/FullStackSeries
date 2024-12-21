import React, { useState } from "react";

function UseState() {
  const [count, setCount] = useState(0);
  return (
    <div className="w-full h-auto mt-10 px-5 py-4 bg-gray-900 rounded-md">
      <h1 className="text-xl font-bold text-center">This is about useState</h1>

      <div className="w-3/12 p-4 mt-5 bg-gray-800 flex flex-col items-center rounded-lg mx-auto">
        <h3 className="text-xl font-semibold text-center mb-5" style={{ color: count === 0 ? "red" : "green" }}>The Value: {count}</h3>
        <button
          className="m-2 p-3 text-white bg-green-600 rounded-md outline-none"
          onClick={() => {
            setCount(count + 1);
          }}
        >
          Increment
        </button>
        <button
          className="m-2 p-3 text-white bg-red-600 rounded-md outline-none"
          onClick={() => {
            if(count > 0){
                setCount(count - 1);
            }else{
                alert("Value can't be negative");
                console.log("Value can't be decremented more than 0"); // This will be shown in the console
            }
          }}
        >
          Decrement
        </button>
      </div>
    </div>
  );
}

export default UseState;
