import React from 'react'
import PropTypes from "prop-types"; // Importing the PropTypes from the prop-types package

// Defining the PropTypes for the Props component
Props.propTypes = {
  name: PropTypes.string.isRequired,
  age: PropTypes.number.isRequired,
  bio: PropTypes.string,
};

function Props(props) {

    // If no "props elems" are passed in the "app.jsx", the default props will be used
    Props.defaultProps = {
        name: "Unknown",
        age: "N/A",
        bio: "No bio available"
    }

  return (
    <div className='w-56 h-auto px-5 py-4 bg-blue-700 rounded-md'>
        <h1 className='text-lg text-white font-bold'>Name: {props.name}</h1>
        <h3 className='text-lg text-white '>Age: {props.age}</h3>
        <h3 className='text-lg text-white '>Bio: {props.bio}</h3>
        {/* Children props - when we pass something not as an argument */}
        <div className='text-white-600 text-sm bg-slate-700 rounded-md'>{props.children}</div> 
    </div>
  )
  
}

export default Props
