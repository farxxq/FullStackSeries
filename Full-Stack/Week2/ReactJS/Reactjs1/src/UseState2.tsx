import React from "react";
import { useState } from "react";

function UseState2() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`Name: ${formData.name}, Email: ${formData.email}`);
  };

  return (
    <>
      <h1 className="mt-10 mb-5 text-3xl text-center font-bold">
        The Form stuff using the UseState methods
      </h1>
      <div className="flex justify-center gap-4 mb-10">
        <div className="w-fit bg-gray-700 p-10 rounded-md">
          <form action="" className="flex flex-col gap-3">
            <input
              type="text"
              name="name"
              placeholder="Enter your Name"
              className="p-2 text-black bg-slate-200 w-auto h-auto outline-none rounded-md"
              onChange={handleChange}
            />
            <input
              type="email"
              name="email"
              placeholder="Enter your Email"
              className="p-2 text-black bg-slate-200 w-auto h-auto outline-none rounded-md"
              onChange={handleChange}
            />
            <button
              type="submit"
              className="m-2 p-2 w-20 text-center text-white bg-blue-600 rounded-md outline-none"
              onClick={handleSubmit}
            >
              Click me
            </button>
          </form>
        </div>
        <div className="mt-10 p-5 min-w-72 flex flex-col gap-4 text-center bg-slate-700 rounded-md">
          <h1 className="text-white text-xl">Form Data</h1>
          <input
              type="text"
              name="name"
              value={formData.name}
              placeholder="Enter your Name"
              className="p-2 text-black bg-slate-200 w-auto h-auto outline-none rounded-md"
            />
            <input
              type="email"
              name="email"
              value={formData.email}
              placeholder="Enter your Email"
              className="p-2 text-black bg-slate-200 w-auto h-auto outline-none rounded-md"
            />
        </div>
      </div>
    </>
  );
}

export default UseState2;
