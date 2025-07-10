import React, {useState} from "react";
import Box from "@mui/material/Box";
import FormControl from '@mui/material/FormControl';
import {InputLabel, Select} from "@mui/material";
import MenuItem from '@mui/material/MenuItem';


type Props = {
    onNivelChange: (nivel: NiveisDetalhe) => void;
    onColorChange: (cor: Cores) => void;
}

const NiveisDetalhe = {
    alto: "HIGH",
    medio: "MEDIUM",
    baixo: "LOW",
}

const coresArray = ["red", "black", "blue"];
const niveisDetalhesArray = ["HIGH", "MEDIUM", "LOW"];

export const MenuComponent: React.FC<Props> = ({ onNivelChange, onColorChange}) =>{
    const [nivelDetalhe, setNivelDetalhe] = useState(NiveisDetalhe.medio);
    const [cores, setCores] = useState([coresArray[1]]);

    const handleChange = (event) => {
        const {
            target: { value },
        } = event;
        const coresData = typeof value === 'string' ? value.split(',') : value;
        setCores(coresData);
        onColorChange(coresData);
    };

    return(<Box sx={{display: 'flex', flexDirection: 'row',width: '50%', margin: "0 auto"}}>
        <FormControl fullWidth>
            <InputLabel id={"Nivel"}>Nivel de Detalhe</InputLabel>
            <Select
                value={nivelDetalhe}
                defaultValue={NiveisDetalhe.medio}
                label={"detalhe"}
                onChange={(event)=>{
                    setNivelDetalhe(event.target.value);
                    onNivelChange(event.target.value)
                }
                }
            >
                {niveisDetalhesArray.map((detalhe) => {
                    return <MenuItem value={detalhe}>{detalhe.toString()}</MenuItem>
                }
                )
                }
            </Select>
        </FormControl>
        <FormControl fullWidth>
            <InputLabel id={"Cor"}>Cor</InputLabel>
            <Select
                value={cores}
                label="cores"
                multiple
                onChange={(event)=> handleChange(event)}
            >
                {coresArray.map((cor) => {
                        return <MenuItem value={cor}>{cor.toString()}</MenuItem>
                    }
                )
                }
            </Select>
        </FormControl>
    </Box>)
}