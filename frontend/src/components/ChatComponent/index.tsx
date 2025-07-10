import React, {type JSX, useState} from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import SendIcon from '@mui/icons-material/Send';
import Paper from '@mui/material/Paper';
import Divider from '@mui/material/Divider';
import {Button, Stack, type Theme} from "@mui/material";
import {MenuComponent} from "../MenuComponent/Menu.tsx";

type Message = {
    sender: 'user' | 'printer';
    content: string | JSX.Element;
    timestamp: string;
};

type Props = {
    id: string;
    chatLog: Message[];
    onSend: (userMessage: string, nivelDetalhe: string, cor:string[]) => void;
    theme: Theme;
    handleOpenModal: (message: string) => void;
    handleAceitar: (image: any) => void;
    handleRedo: (image: any) => void;
};
const NiveisDetalhe = {
    alto: "HIGH",
    medio: "MEDIUM",
    baixo: "LOW",
}
const Cores = {
    PRETO: 'black',
    VERMELHO: 'red',
    AZUL: 'blue'
}

export const ChatComponent: React.FC<Props> = ({ id, chatLog, onSend, theme, handleOpenModal, handleAceitar, handleRedo }) => {
    const [input, setInput] = useState('');
    const [nivelDetalhe, setNivelDetalhe] = useState(NiveisDetalhe.medio);
    const [cores, setCores] = useState([Cores.PRETO]);

    const handleSend = () => {
        const trimmed = input.trim();
        if (trimmed.length > 0) {
            console.log(trimmed);
            onSend(trimmed, nivelDetalhe, cores);
            setInput('');
        }
    };


    return (
        <Box
            sx={{
                display: 'flex',
                flexDirection: 'column',
                height: '90vh',
                padding:4
            }}
            theme={theme}
        >
            <MenuComponent onNivelChange={setNivelDetalhe} onColorChange={setCores}/>

            <Paper
                sx={{
                    flex: 1,
                    p: 2,
                    overflowY: 'auto',
                    borderRadius: 2,
                    width:'100%',
                    flexGrow:1
                }}
                elevation={2}
            >
                {chatLog.length === 0 ? (
                    <Typography color="text.secondary" align="center">
                        Mande uma ideia de Prompt para a impressora!
                    </Typography>
                ) : (
                    chatLog.map((msg, index) => (
                        <Box
                            key={index}
                            sx={{
                                display: 'flex',
                                flexDirection: 'column',
                                alignItems: msg.sender === 'user' ? 'flex-end' : 'flex-start',
                                mb: 1.5,
                            }}
                        >
                            <Box
                                sx={{
                                    px: 2,
                                    py: 1,
                                    bgcolor: msg.sender === 'user' ? 'primary.main' : 'grey.300',
                                    color: msg.sender === 'user' ? 'white' : 'black',
                                    borderRadius: 2,
                                    maxWidth: '75%',
                                }}
                            >
                                <Typography variant="body2">{msg.content}</Typography>
                                { msg.sender === 'printer' && index===(chatLog.length-1) ?
                                <Stack gap={2} sx={{display:'flex', flexDirection:'row'}}>
                                    <Button variant="filled" onClick={()=>{
                                        handleAceitar(msg.img)}}>Aceitar</Button>
                                    <Button variant="filled" onClick={()=>{handleRedo(msg.img)}}>Refazer</Button>
                                    <Button id={"editar"} key={"editar"} variant="filled" onClick={()=>handleOpenModal(msg.img)}>Editar</Button>
                                </Stack>: ""
                                }
                            </Box>
                            <Typography variant="caption" color="text.secondary" sx={{ mt: 0.5 }}>
                                {new Date(msg.timestamp).toLocaleTimeString()}
                            </Typography>
                        </Box>
                    ))
                )}
            </Paper>

            <Divider sx={{ my: 1 }} />

            <Box sx={{ display: 'flex', gap: 1, position:"relative", bottom: 0}}>
                <TextField
                    fullWidth
                    placeholder="Digite um Prompt..."
                    variant="outlined"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSend()}
                />
                <IconButton color="primary" onClick={handleSend}>
                    <SendIcon />
                </IconButton>
            </Box>
        </Box>
    );
};