import {SendChatInput, GetChatInput, Chat} from "./types.ts";
import {useFetch} from "../hooks/fetchHook.ts";


export const useGetChats = () =>{
    const { commonFetch, isLoading, data} = useFetch<Chat>({
        url: 'http://localhost:8080/api/chats/get',
    });

    const getChat = (input: GetChatInput) => commonFetch({ input, method: "GET" });

    return { getChat, isLoading, data };
}

export const useSendMessage = () => {
    const { commonFetch, isLoading, data } = useFetch<Chat>({
        url: 'http://localhost:8080/api/chats/send-message',
    })

    const sendMessage = (input: SendChatInput) => commonFetch({input, method: 'POST'});

    return { sendMessage, isLoading, data};

}